import os
import socket

hostname = socket.gethostname()
ipaddr = str(socket.gethostbyname(hostname))
IP = str("IP Address: ")
print(hostname)
print (str(IP) + str(ipaddr))
print(os.getcwd())
