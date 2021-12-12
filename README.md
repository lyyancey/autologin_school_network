# 自动连接`DMU`的校园网脚本

## 环境

### 浏览器

Chrome 版本为： 96.0.4664.93（正式版本） （64 位）

浏览器可以选择火狐或者其他的，但是要有对应的**驱动**， 还要修改代码，所以建议没有Chrome浏览器的可以装一个。

Chrome版本的查看方式为:

浏览器右上角三个点------->帮助---------------->关于Google Chrome

### 浏览器对应的驱动

- 下载Chrome的驱动:[点这里](https://chromedriver.chromium.org/downloads), 浏览器驱动的版本要和你自己的浏览器版本对应，不然会报错。
- 下载下来之后解压，解压之后会有一个`chromedriver.exe`文件，将这个文件所在的***目录*** 添加到系统变量（PATH）中。

### 代码环境

- 打开`Anaconda Prompt` 输入命令`conda create -n autologin python=3.4`,这里***不能***是别的python版本， python环境的名字可以任意。
- 切换到新建的环境下`conda activate autologin`。
-  安装依赖包：`pip install selenium `

### 修改代码里面的参数

- 首先打开`git`将代码下载下来`git clone git@github.com:lyyancey/autologin_school_network.git`
- 打开`autologin.py`在94、95行的位置分别填上你自己的学号和校园网密码。
- 打开`run.bat`文件，将第4行的位置改成你的`activate.bat`脚本所在的位置，(`activate.bat`这个脚本在你自己的anaconda安装目录下)
- 将`run.bat`文件中的第5行的环境名称改成你自己创建的环境名称
- 将`run.bat`文件中的第7行改成代码在你的电脑上的路径即可。

### 将`run.bat`加到Windows 任务计划当中

怎么加可以参考[这里](https://github.com/lyyancey/daily_report)

### 注意事项

- 不要在挂代理的情况下使用`Anaconda Prompt`,不然会报错。
- 不要在挂代理的情况下使用这个脚本，否则连不上校园网。

![Alt](https://repobeats.axiom.co/api/embed/f4dd2058df9141bd2b115eba406370069e1fe7db.svg "Repobeats analytics image")