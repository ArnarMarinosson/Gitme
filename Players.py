import socket
import select
import sys
import time
import random

class Players():

    def __init__(self, team, playername):
        self.team = ''
        self.playername = ''

# Leikmaður velur sér lið
    def getTeam(self,c,c2):
        while True:
            #try:
            msg = 'Pick a nation' '\n'
            c.send(bytes(msg, 'utf-8'))
            time.sleep(1)
            buf = c2.recv(1024)
            msg = buf.decode('utf-8')

            if msg == 'A':
                self.team = 'Argentina'
            elif msg == 'I':
                self.team = 'Iceland'
            elif msg == 'N':
                self.team = 'Nigeria'
            else:
                self.team = 'Croatia'
            break

    def getPlayer(self, c, c2):
        while True:
            msg = 'You picked '+self.team+', now pick a player''\n'
            c.send(bytes(msg, 'utf -8'))
            buf = c2.recv(1024)
            msg = buf.decode('utf -8')
            self.playername = msg
            print(self.playername)
            break

def main():
    s = socket.socket(socket.AF_INET , socket. SOCK_STREAM)
    s2 = socket.socket(socket.AF_INET , socket. SOCK_STREAM)
    port = 3030
    port2 = 3031
    cnt=0
    print('test0')
    try:
        s.bind (('',port))
        s2.bind (('',port2))
    except socket.error as msg:
        print( 'Bind failed - aborting' )
        sys.exit ()

    s.listen (5)
    s2.listen (5)
    #c,addr = s.accept()
    #c2,addr2 = s2.accept()
    #print('New connection:', addr)
    #print('New connection:', addr2)

    team = 'I'
    player = '10'
    tem = Players(team,player)

    #tem.getTeam()
    #tem.getPlayer()
    while True:
        c,addr = s.accept()
        c2,addr2 = s2.accept()
        print('New connection:', addr)
        print('New connection:', addr2)
        c.send(b'Hello\n')
        cnt += 1
        time.sleep (1)
        msg='Your id is '+str(cnt)+'\n'
        c.send(bytes(msg ,'utf -8'))
        print('test2')
        tem.getTeam(c,c2)
        print('test3')
        tem.getPlayer(c,c2)
        #print('test3')

    s.close()
    s2.close()

if __name__ == '__main__':
    main()
