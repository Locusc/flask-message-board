# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
自定义命令函数
"""

import click
from flaskmessageboard import app, db


# 注册一个flask命令
from flaskmessageboard.models import Message

'''
使用click提供的option装饰器为命令添加数量选项--count 使用default关键字将默认值设为20
为了方便测试 生成虚拟数据前会删除重建数据库表
'''
@app.cli.command()
@click.option('--count', default=20, help='Quantity of messages, default is20.')
def forge(count):
    """Generate fake messages."""
    from faker import Faker

    db.drop_all()
    db.create_all()

    fake = Faker()
    click.echo('Working...')

    for i in range(count):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(message)

    db.session.commit()
    click.echo('Created %d fake messages.' % count)