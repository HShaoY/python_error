#!/usr/bin/env python
#listen

import sys
import socket
import traceback

host = ''
port = 8888

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.bind((host,port))

s.listen(5)

'''while(1):
    clientsock,clientaddr = s.accept()
    print "connect from ",clientsock.getpeername()
    clientsock.close()
'''
while(1):
    try:
        clientsock,clientaddr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue
    try:
        print "connect from",clientsock.getpeername()
    except (KeyboardInterrupt,SystemExit):
        raise
    except:
        traceback.print_exc()
    try:
        clientsock.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
