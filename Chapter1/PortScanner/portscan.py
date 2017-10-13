
# Checks if sockets can connect to open ports
# Author: Sid

import socket
import os, sys

host = '10.163.48.75'
portL = [21,22,23,25,53,80,111,139,445,512,513,514,1099,1524,2049,2121,3306,5432,5900,6000,6667]

def main():
    socket.setdefaulttimeout(2)
    for port in portL:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            banner = s.recv(1024)
            if not banner:
                print '[-] No banner retrieved but connected to %s \n' % (port)
            print '[+] Connected to %s! Banner retrieved: %s \n' % (port, banner)
            s.close()
        except Exception, e:
            print '[-] Exception caught: %s on port: %s \n' % (e, port)

if __name__ == '__main__':
    main()