# 发邮件短信的打杂系统

## configure
在你的shell环境变量中，export
```
export mail_host=smtp.163.com
export mail_user=username@website.com
export mail_pass=`password`
```

## usage

http://127.0.0.1:5000/sendmail

only support `POST` HTTP methods.

|Parameters|Required|Description|
|:---:|---|---|
|s|Yes|subject|
|t|Yes|text|
|r|Yes|receivers|

## example
```
http://127.0.0.1:5000/sendmail
post data:
r
xxxx@139.com,xxxxx@qq.com
s
test
t
http://avatar.csdn.net/6/8/C/1_z_johnny.jpg
```

## TODO
support TLS(standard encryption)
