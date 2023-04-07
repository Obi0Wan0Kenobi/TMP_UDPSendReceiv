from socket import *
import sys

s = socket(AF_INET,SOCK_DGRAM)
host ="localhost"
port = 9999
buf =1024
addr = (host,port)

file_name="check.txt"

s.sendto((file_name+"1").encode(),addr)

f=open(file_name,"rb")
data = f.read(buf)
while (data):
    if(s.sendto(data,addr)):
        print("sending ...")
        data = f.read(buf)
s.close()
f.close()