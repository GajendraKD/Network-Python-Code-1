#!/usr/bin/python
import socket
def remotehostinfo():
        rhost = raw_input("Enter remote hostname: ")
        rip = socket.gethostbyname(rhost)
        try:
                print "IP address of remote host is : ", rip
        except socket.error, err_msg:
                print "Error"

remotehostinfo()
