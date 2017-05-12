# 发邮件短信的打杂系统

## configure
在你的shell环境变量中，export
```
export mail_host=smtp.ym.163.com
export mail_user=username@website.com
export mail_pass=`password`
```

## usage

http://127.0.0.1:5000/sendmail


|name|argument(s)|Condition|
|:---:|---| ---|
|s|subject||
|t|text||
|r|receivers||
