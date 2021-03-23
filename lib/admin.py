import requests, os, PIL
from PIL import Image

class main():
    csrftoken = ""
    password = ""
    session  = requests.Session()
    status = False

    def __init__(self) -> None:
        self.sniffer()

    def sniffer(self):
        r= self.session.get("http://172.16.154.130:8800/")
        sourceCode = r.text
        self.csrftoken = sourceCode.split('<meta name="csrf-token" content="')[1].split('">')[0]
        captichaUrl = sourceCode.split('<img id="loginform-verifycode-image" src="')[1].split('" alt="">')[0]
        self.capticha(captichaUrl)
        return sourceCode

    def capticha(self,url):
        r = self.session.get("http://172.16.154.130:8800"+url)
        a = r.content
        with open ('1.jpg','wb') as f:
            f.write(a)
        """
        im = Image.open('./1.jpg')
        im.show()
        return input()
        """
    
    def log(self,capticha,username,password,typ):
        if typ =="login":
            data={
                "_csrf":self.csrftoken,
                "LoginForm[username]":username,
                "LoginForm[password]":password,
                "LoginForm[verifyCode]":capticha,
                "login-button":""
            }
            r = self.session.post("http://172.16.154.130:8800/",data=data)
        elif typ=="logout":
            data={
                "_csrf":self.csrftoken
            }
            r = self.session.post("http://172.16.154.130:8800/site/logout",data=data)
        return r.text
    
    def return_analysis(self,returning):
        capticha_error = "验证码错误"
        password_error = "用户名或密码错误"
        success = "产品信息"
        if capticha_error in returning:
            pass
        if password_error in returning:
            pass
        if success in returning:
            print("login_success")
            self.status = True
            return returning
    
    def offline(self,sourceCode):
        if self.status == False:
            print("login err")
        offline_url = sourceCode.split('<a class="btn btn-xs btn-danger" href="')[1].split('"')[0]
        offline_url = "http://172.16.154.130:8800" + offline_url
        data={
            "_csrf":self.csrftoken
        }
        self.session.post(offline_url,data=data)
        return "success"

    def analysis(self):
        #获取csrf信息
        returning = self.log("abcd","202020020504","111111","login")
        #模拟登陆
        result = self.return_analysis(returning)
        #获取源代码(登出id)
        self.offline(result)
        #登出
        

#main().analysis()