import socket
import select
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost',3002))
while True:
    # read , write , exception , 3 sec timeout
    ready = select.select([s],[],[],3)
    if len(ready) < 1:
        break
    buf = s.recv(1024)
    if len(buf) == 0: # EOF, socket closed
        break
    msg = buf.decode('utf-8')
    print(msg,end='')
    s.close()
