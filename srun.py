import sys,os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject, pyqtSlot, QUrl
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView
import Core as Core

#本类为python和js信息交换内容
class Receivers(QObject):
    # pyqtSlot
    @pyqtSlot(str, result=str)
    def testTxt(self, content):
        pass

    @pyqtSlot(str, result=str)
    def Login(self,content):
        UserName = content.split('\n')[0]
        PassWord = content.split('\n')[1]
        core.username = UserName
        core.password = PassWord
        self.returning(core.login())

    @pyqtSlot(str, result=str)
    def Logout(self,code):
        self.returning(core.logout())

    def js_callback(self,result):
        print(result)

    @pyqtSlot(str, result=str)
    def show_status(self):
        status = core.show_status()
        command = "Show('status','"+status+"');"
        browser.page().runJavaScript(command)

    def returning(self,content):
        '''返回例如登陆信息'''
        command = "dialog('"+content+"');"
        browser.page().runJavaScript(command)



    @pyqtSlot(str, result=str)
    def exit_app(self):
        QApplication.quit()

#构建主页
if __name__ == "__main__":
    core = Core.obj()
    core.__init__
    app = QApplication(sys.argv)
    # 新增一个浏览器引擎
    browser = QWebEngineView()
    browser.setWindowTitle("Srun3K Login")
    browser.resize(900, 600)
    # 增加一个通信中需要用到的频道
    channel = QWebChannel()
    # 通信过程中需要使用到的功能类
    Receiver = Receivers()
    # 将功能类注册到频道中，注册名可以任意，但将在网页中作为标识
    channel.registerObject("Receivers", Receiver)
    # 在浏览器中设置该频道
    browser.page().setWebChannel(channel)
    # 内置的网页地址
    url_string = os.getcwd().replace("\\","/") + "/index.html"
    #Windows下有"/"和"\"的区别
    print(url_string)
    browser.load(QUrl(url_string))
    browser.show()
    sys.exit(app.exec_())
