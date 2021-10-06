# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 21:33:37 2021

@author: ASUS
"""

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(('0.0.0.0',9999))
print('I am connecting the sever!')
for data in['aBch','f服务d','h7Tq','.']:
   s.send(data.encode('utf-8'))
   str1=s.recv(1024)
   str2=str(str1,encoding='utf-8')
   print('The original string is:',data,'\tthe processed string is:',str2)
s.close()


