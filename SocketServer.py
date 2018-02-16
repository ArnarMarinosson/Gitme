import socket
import sys
import time
# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 3002
cnt =0
try:
    s.bind(('',port))
except socket.error as msg:
    print( 'Bind failed - aborting ')
    sys.exit()
s.listen(5)
print('Test#1')
while True:
    print('Test#2')
    c,addr = s.accept()
    print('New connection:', addr)
    c.send(b'Hello\n')
    cnt += 1
    time.sleep(1)
    msg='Your id is '+str(cnt)+'\n'
    c.send(bytes(msg,'utf-8'))
    c.close()
