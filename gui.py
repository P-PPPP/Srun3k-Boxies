# -*- coding: UTF-8 -*-

import webview,webbrowser,os
from lib import core
import os


class Api():
    '''与页面交互'''
    def login(self,info):
        core.username = info.split('\n')[0]
        core.password = info.split('\n')[1]
        loginInfo = core.login()
        window.evaluate_js("dialog('"+loginInfo+"')")
        window.evaluate_js("useageCount('"+loginInfo+"')")
    def status(self):
        window.evaluate_js("Status('"+core.show_status()+"')")
    def destory(self):
        window.destroy()
    def logout(self):
        #webbrowser.open_new_tab("http://172.16.154.130:8800/home")
        print(core.logout())
    def hotspot(self):
        os.system("start ms-settings:network-mobilehotspot")


def getConfig():
    openInfo = open("config.json")
    info = openInfo.read()
    openInfo.close()
    return info

        


if __name__ == '__main__':
    core = core.obj()
    core.getConfig(getConfig())
    api = Api()
    url = "file:" + os.getcwd().replace("\\","/") + "/index.html"
    #url = "index.html"
    window = webview.create_window(title="SrunBoxies",url=url,frameless=True,js_api=api)

    webview.start(api.destory,window)
