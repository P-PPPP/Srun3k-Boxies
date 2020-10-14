![图片.png](https://i.loli.net/2020/10/14/GN4PgavIsTfYhje.png)
### SrunBoxies 深澜盒子
#### 特点
- [ 使用python+pywebview编写,理论上适用于所有平台 ]
- [ Windows下编译过后只有10mb，更加简洁 ]
- [ 使用MaterialDesign美化,界面简洁清爽 ]
- [ 前后端分离,便于维护和升级, 函数库可直接调用 ]
- [ 强制下线服务 ]
- [curl命令组合工具，可使用路由器/软路由多拨(暂时下线)]

#### 缺点
- 体积过大QWQ(已于最近版本修复，更新了技术栈，改用webview作为框架而非qt)

#### ToDo List
- Windows下开机启动
- CLI
#### 特别感谢
很多功能只是在 [原版项目](https://github.com/ehaut/srun3k-client/tree/pyqt5) 上修改的，狗尾续貂罢了，可惜项目已经存档，感谢[@zengxs](https://github.com/zengxs) [@noisky](https://github.com/noisky)
同时感谢[mdui](https://github.com/zdhxiong/mdui)的material界面框架
#### 使用方法
Windows用户前往release页面下载解压，打开```gui.exe```，如要配置登陆地址和信息，请自行修改目录下的```config.json```文件
其他系统用户请参考[源码使用](https://github.com/peterpei1186861238/Srun3k-Boxies/blob/master/README.md#%E6%BA%90%E7%A0%81%E4%BD%BF%E7%94%A8)
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
```.\venv\Lib\site-packages\webview\lib\WebBrowserInterop.x64.dll
.\venv\Lib\site-packages\webview\lib\WebBrowserInterop.x86.dll
.\venv\Lib\site-packages\webview\lib\Microsoft.Toolkit.Forms.UI.Controls.WebView.dll
```
这三个文件到文件目录中(可在python目录中找到)
Windows下编译命令为```pyinstaller --add-data "WebBrowserInterop.x86.dll;./" --add-data "WebBrowserInterop.x64.dll;./" --add-data "Microsoft.Toolkit.Forms.UI.Controls.WebView.dll;./" --add-data "Microsoft.Toolkit.Forms.UI.Controls.WebView.LICENSE.md;./" gui.py```可自行添加图标等文件
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





