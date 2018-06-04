import getpass
import telnetlib

user= raw_input("Enter Telnet Username: ")
password= getpass.getpass()

f= open("switchip")

for line in f:
        print"Getting running conf Copy" + (line)
        HOST= line.strip()
        tn= telnetlib.Telnet(HOST)

        tn.read_until("Username: ")
        tn.write(user +"\n")
        if password:
                tn.read_until("Password: ")
                tn.write(password +"\n")

        tn.write("enable\n")
        tn.write("term len 0\n")
        tn.write("show running-config\n")
        tn.write("exit\n")

        readoutput= tn.read_all()
        saveoutput= open("Switch" +HOST,"w")
        saveoutout.write(readoutput)
        saveoutput.write("\n")
        saveoutput.close
