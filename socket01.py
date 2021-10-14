import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('s=', s);
s.connect(('10.1.8.65',80));
print('s=', s)
s.send(b'GET / HTTP/1.1\r\nHost:www.qjnu.edu.cn\r\nConnection:close\r\n\r\n')
buffer=[]
while True:
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
s.close()
data=b''.join(buffer)
header, html=data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
with open('qjnu.html', 'wb')as f:
    f.write(html)