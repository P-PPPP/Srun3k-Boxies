![图片.png](https://i.loli.net/2021/03/23/qZN4sQ9OTkdb1np.png)
### SrunBoxies 深澜盒子
[相关教程](http://wordpress.peterfile.top/index.php/2020/09/26/%e6%b7%b1%e6%be%9c%e6%a0%a1%e5%9b%ad%e7%bd%91%e6%8a%98%e8%85%be%e6%8c%87%e5%8d%97/)
#### 特点
- [ 使用python+pywebview编写,理论上适用于所有平台 ]
- [ Windows下编译过后只有10mb，更加简洁 ]
- [ 使用MaterialDesign美化,界面简洁清爽 ]
- [ 前后端分离,便于维护和升级, 函数库可直接调用 ]

#### ToDo List
- Windows下开机启动
- CLI
#### 特别感谢
很多功能只是在 [原版项目](https://github.com/ehaut/srun3k-client/tree/pyqt5) 上修改的，狗尾续貂罢了，可惜项目已经存档，感谢[@zengxs](https://github.com/zengxs) [@noisky](https://github.com/noisky)
同时感谢[mdui](https://github.com/zdhxiong/mdui)的material界面框架
#### 使用方法
Windows用户前往release页面下载解压，打开```gui.exe```，如要配置登陆地址和信息，请自行修改目录下的```config.json```文件
</br>Centos和其他Linux用户下载Linux版，解压后cd到文件目录，终端输入```gui```
其他系统用户请参考[源码使用](#%E6%BA%90%E7%A0%81%E4%BD%BF%E7%94%A8)
#### 源码使用
1. 安装python3 以及 pip
2. 执行下方命令安装必要库
```
pip install requirements.txt -i https://pypi.doubanio.com/simple/
```
3. 终端打开到相应目录下执行
```
python3 gui.py
```
#### 编译
编译请先安装```pyinstaller```</br>
Windows用户请复制
```
.\venv\Lib\site-packages\webview\lib\WebBrowserInterop.x64.dll
.\venv\Lib\site-packages\webview\lib\WebBrowserInterop.x86.dll
.\venv\Lib\site-packages\webview\lib\Microsoft.Toolkit.Forms.UI.Controls.WebView.dll
```
这三个文件到文件目录中(可在python目录中找到)
Windows下编译命令为</br>
```pyinstaller -F gui.py --add-data "WebBrowserInterop.x86.dll;./" --add-data "WebBrowserInterop.x64.dll;./" --add-data "Microsoft.Toolkit.Forms.UI.Controls.WebView.dll;./"  --noconsol -i 1.ico```</br>
可自行添加图标等文件</br>
需要注意的是，在Windows用户必须以非管理员账户编译，否则有概率在打开时报错，这是调用默认Edge内核会出现的问题，除此之外，你也可以自行编译CEF版本，具体请参考[官方文档](https://pywebview.flowrl.com/guide/renderer.html#gtk-webkit2)
</br>其他系统用户自行修改

#### 文件结构
```
srun.py 为qt界面
Core.py 为核心函数
config.json 为配置文件
```
#### 已知bug(其实也算不上啦)
暂时无法触发Windows的自动休眠
#### 开源相关
遵守[GPLＶ３](https://github.com/peterpei1186861238/Srun3k-PyQt/blob/master/LICENSE)开源协议，欢迎PR，　提issue





