import json,os,requests

class obj():    
    username=""
    password=""

    def __init__(self):
        '''初始化类'''
        super().__init__()
        self.session = requests.Session()
        self.config = self.getConfig()

    
    def getConfig(self):
        '''获取配置信息'''
        infoOpen = open("config.json")
        info = infoOpen.read()
        infoOpen.close()
        global config
        config = json.loads(info)
        return config

    def login(self):
        '''登陆'''
        password_enc = self.password_encrypt(self.password,
                                             self.config['options']['secret'])
        payload = {
            "action": "login",
            "username": self.username_encrypt(self.username),
            "password": password_enc,
            "mac": self.config['options']['mac'],
            "ac_id": self.config['options']['acid'],
            "drop": 0,
            "pop": 1,
            "type": 10,
            "n": 117,
            "mbytes": 0,
            "minutes": 0,
        }
        r = self.session.post(
            self.config['server']['url']['portal'], data=payload)
        status = r.text
        return status
        

    def logout(self):
        '''登出'''
        payload = {
            "action": "logout",
            "username": self.username,
            "ac_id": self.config['options']['acid'],
            "type": 10,
        }
        r = self.session.post(
            self.config['server']['url']['portal'], data=payload)
        status = r.text
        return status

    def show_status(self):
        '''状态显示'''
        r = self.session.get(self.config['server']['url']['info'])
        status = r.text
        return status

    #加密方法
    @staticmethod
    def username_encrypt(username):
        result = '{SRUN3}\r\n'
        return result + ''.join([chr(ord(x) + 4) for x in username])

    @staticmethod
    def password_encrypt(password, key='1234567890'):
        result = ''
        for i in range(len(password)):
            ki = ord(password[i]) ^ ord(key[len(key) - i % len(key) - 1])
            _l = chr((ki & 0x0F) + 0x36)
            _h = chr((ki >> 4 & 0x0F) + 0x63)

            if i % 2 == 0:
                result += _l + _h
            else:
                result += _h + _l
        return result