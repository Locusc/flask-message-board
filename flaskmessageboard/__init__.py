# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

'''
每一个包含__init__.py文件的文件夹都被视为包
包可以使用文件夹来组织模块
__init__通常被称为构造文件 可以为空
可也可以用来放置包的初始化代码 当包或包内的模块被导入时 构造文件将被自动执行

使用包组织程序代码后 创建程序实例
'''


# flaskmessageboard的核心组件都放在一个包中 称为程序包
# 包通常使用程序名称 有时为了方便管理也会使用app作为包名称
'''
因为flask通过这个值来确认程序路径 当使用包组织代码时
为了确保其他扩展或测试框架获得正确的路径 最好使用硬编码的形式写出包名称作为程序名称

除了直接写出包名称 也可以从__name__变量获取包名称 即app=Flask(__name__.split('.')[0])
'''
app = Flask('flaskmessageboard')

# 在创建程序实例后 from_profile()方法即可加载配置 传入配置模块的文件名作为参数
app.config.from_pyfile('settings.py')

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

'''
当启动程序时 首先被执行的是包含程序实例的脚本 即构造函数
但注册在程序实例上的各种处理程序均存放在其他脚本中
比如视图函数view.py 错误处理函数error.py
如果不被执行 那么这些视图函数和错误处理函数就不会注册到程序上
那么程序也无法正常运行
为了让使用程序实例app注册的视图函数 错误函数 自定义命令函数和程序实例关联起来
需要在构造文件中导入这些模块 因为这些模块也需要从构造文件中导入程序实例
所以为了避免循环依赖  这些导入语句在构造文件的末尾定义
'''
from flaskmessageboard import view, errors, commands


'''
从构造文件中导入变量时不需要注明构造文件的路径
只需要从包名称导入 比如导入构造文件中定义的程序实例app可以使用from flaskmessageboard import app

Flask通过FLASK_APP环境变量定义的模块中寻找程序实例 所以在启动程序前
需要给.flaskenv中的环境变量FLASK_APP重新赋值 
这里仅写出包名称即可
FLASK_APP = flaskmessageboard
'''
