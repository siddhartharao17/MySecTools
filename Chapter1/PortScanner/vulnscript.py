
# FTP Vuln-Detection script
# Author: Sid

import socket
import sys
import os

def retBanner(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        banner = s.recv(1024)
        # print type(banner)
        # banner = banner.decode('utf-8')
        return banner,s

        # else:
        #     print '[-] Cannot connect to %s \n' % (port)
    except Exception, e:
        print '[-] Exception caught: %s on port: %s \n' % (e, port)

# def checkVuln(filename, banner):
#     fp = open(filename, "r")
#     for vuln in fp.readlines():
#         if vuln.strip('\n') in banner.strip('\n'):
#             print "[+] Server is vulnerable: %s" % str(banner.strip('\n'))

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print "[-] File %s does not exist!" % str(sys.argv[1])
            exit(0)

        if not os.access(filename, os.R_OK):
            print "[-] File %s: Permission Denied." % str(sys.argv[1])
            exit(0)

    else:
        print "[-] Usage: python vulnscript.py <vuln filname>"
        exit(0)

    portList = [21,22,23,25,53,80,111,139,445,512,513,514,1099,1524,2049,2121,3306,5432,5900,6000,6667]
    # subnet = "10.163.48."           # 10.163.48.0/24
    # for host in range(1,255):
    # ip = subnet + str(43)     # IP address
    host = '10.163.48.75'
    for port in portList:
        banner,s = retBanner(host, port)
        if not banner:
            print '[-] No banner retrieved but connected to %s \n' % (port)
        else:
            print '[+] Connected to %s! Banner retrieved: %s \n' % (port, banner)
        s.close()
        # if banner:
        #     print "[+] IP %s #%s : %s" % (host, port, banner)
        #     checkVuln(filename, banner)

if __name__ == "__main__":
    main()