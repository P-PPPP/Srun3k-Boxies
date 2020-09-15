![](https://i.loli.net/2020/09/15/DJnqK7sIMRBrOhG.png)
### Srun client 一个深澜3000登录器
#### 特点
- [ 使用PyQt5编写,理论上适用于所有平台 ]
- [ 使用MaterialDesign美化,界面简洁清爽 ]
- [ 前后端分离,便于维护和升级, 函数库可直接调用 ]
#### ToDo List
- Udp 心跳包
- Windows下开机启动
- ACID自动检测
- 自动登陆和多用户登陆
#### 特别感谢
很多功能只是在 [原版项目](https://github.com/ehaut/srun3k-client/tree/pyqt5) 上修改的，狗尾续貂罢了，可惜项目已经存档，感谢[@zengxs](https://github.com/zengxs) [@noisky](https://github.com/noisky)
#### 使用方法
1. 安装python3 以及 pip3
2. 执行下方命令安装必要库
```
pip install requirements.txt -i https://pypi.doubanio.com/simple/
```
3. 终端打开到相应目录下执行
```
python3 srun.py 或 py srun.py
```
#### 已知bug(其实也算不上啦)
注销用户必须用本应用登陆
#### 开源相关
遵守[GPLＶ３](https://github.com/peterpei1186861238/Srun3k-PyQt/blob/master/LICENSE)开源协议，欢迎PR，　提issue





