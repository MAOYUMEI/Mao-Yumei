Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:23:07) [MSC v.1927 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #coding=utf-8
>>> import smtplib
>>> from email.mime.text import MIMEText
>>> msg_from='3498653289@qq.com'
>>> passwd='bpohntalairecjif'
>>> msg_to='57820048@qq.com'
>>> subject="2019144133毛玉梅"\
	  "本机私网：20.77.186.234"\
	  "本机公网：117.136.84.178"\
	  "学校私网：10.128.64.254"\
	  "学校公网：220.164.161.126"
>>> content="pip install PyEmail"
>>> msg=MIMEText(content)
>>> msg['Subject']=subject
>>> msg['From']=msg_from
>>> msg['To']=msg_to
>>> try:
	s=smtplib.SMTP_SSL("smtp.qq.com",465)
	s.login(msg_from,passwd)
	s.sendmail(msg_from,msg_to,msg.as_string())
	printf("发送成功")
except(s.SMTPException,e):
	printf("发送失败")
finally:
	s.quit()