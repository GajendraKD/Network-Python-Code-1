#!/usr/bin/python
import socket
def localhostinfo():
	h = socket.gethostname()
	i = socket.gethostbyname(h)
	print "Host name : ", h
	print "IP address: ", i
	
localhostinfo()
