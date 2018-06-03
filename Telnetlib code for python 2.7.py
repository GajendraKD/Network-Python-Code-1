import getpass
import sys
import telnetlib
HOST = "192.168.122.80"

user = raw_input("Enter your Username: ")
password = getpass.getpass()

tn= telnetlib.Telnet (HOST)

tn.read_until("Username: ")
tn.write (user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password +"\n")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("config t\n")
tn.write("loopback 0\n")
tn.write("ip address 1.1.1.1 255.255.255.255\n")
tn.write("no shut\n")
tn.write("exit\n")
tn.write("exit\n")

print tn.read_all()
