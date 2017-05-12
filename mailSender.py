#!/usr/bin/env python
# coding:utf8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import config

def mailSender(subject,text,receivers):
    # 第三方 SMTP 服务
    mail_host = config.mail_host  # 设置服务器
    mail_user = config.mail_user  # 用户名
    mail_pass = config.mail_pass  # 口令

    sender = config.sender

    # receivers list
    # receivers = ",".join(receivers)

    # message
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'test message'

    msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="http://avatar.csdn.net/6/8/C/1_z_johnny.jpg"><br>good!','html','utf-8')
    msgRoot.attach(msgText)


    message = MIMEText(text, 'plain', 'utf-8')
    # message['From'] = Header(mail_user, 'utf-8') #代发
    message['To'] = Header(receivers, 'utf-8')


    message['Subject'] = Header(subject, 'utf-8')


    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, msgRoot.as_string())
        print "邮件发送成功"
        return 'success'
    except smtplib.SMTPException:
        print "Error: 无法发送邮件"
        return 'error'

# http://avatar.csdn.net/6/8/C/1_z_johnny.jpg

if __name__ == '__main__':

    mailSender('hhhh','hello',['xxxxx@qq.com','xxxx@gmail.com'])
