# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 15:39:49 2017

@author: hao
"""

import socket
import sys

# Create a TCP/IP socket
PortNo = 10000
IPaddr = '127.0.0.1'
MaxBuf = 128
Timeout = 60 * 1   # 1 min
# Send data
message = '20'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (IPaddr, PortNo)
print(sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    #message = 'Hi'
    print(sys.stderr, 'Sending: '+ message)
    sock.sendall(message.encode(encoding='utf-8'))
   # s.setblocking(0)
   # ready = select.select([s], [], [], timeout)
    #if ready[0]:
    data = sock.recv(MaxBuf)
    print(sys.stderr, 'Received: '+ bytes.decode(data))

finally:
    print(sys.stderr, 'closing socket')
    sock.close()