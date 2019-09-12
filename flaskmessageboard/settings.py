# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import sys

from flaskmessageboard import app

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

# 由于配置文件被放到了程序包内 为了定位到位于项目根目录的数据库文件
# 使用os.path.dirname(app.root_path)获取上层目录
# app.root_path属性存储程序实例所在的路径 数据库URL和密钥都会首先从环境变量获取
dev_db = prefix + os.path.join(os.path.dirname(app.root_path), 'data.db')

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
