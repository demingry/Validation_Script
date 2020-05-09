#coding=utf-8

import requests
import time
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header

url=''
header={'Accept':'text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8','Accept-Encoding':'gzip, deflate','Accept-Language': 'zh-CN','Cache-Control': 'max-age=0','Connection': 'Keep-Alive','Cookie': 'JSESSIONID=A2D0D1F80BE6BCA4B61D5D8C82B8B241','Host': '222.206.176.104','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
mail_host = "[SMTPServer]"
mail_user = "[YourEmail]"
mail_pass = "[Your Password]"
sender = '[MailSender]'
receivers = ['PostMaster@qq.com']
content = 'accessible'
title = 'notice!'


def validate():

    response=requests.get(url,headers=header)

    time.sleep(60)

    html_doc=response.text

    soup=BeautifulSoup(html_doc,'lxml')

    request_url='http://222.206.176.104'+soup.find_all('a')[0]['href']

    request2url=requests.get(url=request_url,headers=header)

    time.sleep(120)

    if request2url.status_code=='200':
        sendEmail()
        exit(0)
    else:
        print('404')
        return 0


def sendEmail():     
    message = MIMEText(content, 'plain', 'utf-8')   
    message['From'] = "{}".format(sender)    
    message['To'] = ",".join(receivers)    
    message['Subject'] = title     
    try:        
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)       
        smtpObj.login(mail_user, mail_pass)       
        smtpObj.sendmail(sender, receivers, message.as_string())       
        print("mail has been send successfully.")     
    except smtplib.SMTPException as e:        
        print(e)

if __name__=='__main__':
    while True:
        validate()
