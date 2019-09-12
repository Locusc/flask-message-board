# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
定义数据库模型
"""

from datetime import datetime
from flaskmessageboard import db


# timestamp字段用来存储每一条留言的发表时间(时间戳)
# 这个字段存储Python的datetime对象
# 设置index = True开启索引 并使用default参数设置了字段默认值
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=datetime.now, index=True)