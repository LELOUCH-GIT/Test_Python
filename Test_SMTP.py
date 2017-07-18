# 以后发邮箱就不用那么麻烦啦
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "15804536790@163.com"  # 用户名
mail_pass = "hehe1234567"  # 口令

sender = '15804536790@163.com'
receivers = ['1901148715@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('这可能是我用Python发的第一个邮件...', 'plain', 'utf-8')
message['From'] = sender
message['To'] = receivers[0]

subject = '我的python第二个邮件'
message['Subject'] = subject

smtpObj = smtplib.SMTP_SSL()
smtpObj.connect(mail_host, 994)  # 25 为 SMTP 端口号
smtpObj.starttls()
smtpObj.login(mail_user, mail_pass)
smtpObj.sendmail(sender, receivers, message.as_string())
smtpObj.quit()
print("邮件发送成功")
