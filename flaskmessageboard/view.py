# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
视图函数
"""
from flask import flash, redirect, url_for, render_template

from flaskmessageboard import app, db
from flaskmessageboard.models import Message
from flaskmessageboard.forms import HelloForm

'''
index视图的两个作用
    1.处理GET请求 从数据库中查询所有的消息记录 返回渲染后的包含消息列表的主页模板index.html
    2.处理POST请求 问候表单提交后 验证表单数据通过验证后将数据保存到数据库中
      使用flash()函数显示一条提示 然后重定向到index视图 渲染页面
'''


@app.route('/', methods=['GET', 'POST'])
def index():

    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)  # 实例化模型类 创建记录
        db.session.add(message)  # 添加记录到数据库会话
        db.session.commit()  # 提交会话
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))  # 重定向到index视图

    # 加载所有的记录
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html', form=form, messages=messages)

