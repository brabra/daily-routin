#!/usr/bin/env python
# coding:utf8
import os
from email.mime.text import MIMEText
from email.header import Header

mail_host = os.environ['mail_host']  # 设置服务器
mail_user = os.environ['mail_user']  # 用户名
mail_pass = os.environ['mail_pass']  # 口令

sender = os.environ['mail_user']

receivers = ['']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

subject = u'test ok'
