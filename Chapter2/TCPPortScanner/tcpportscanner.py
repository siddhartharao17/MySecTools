import optparse
from socket import *

# build connScan to attempt to create a connection to the target host and port
# build portScan to resolve an IP addr to a friendly hostname
def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('ViolentPython\r\n')
        res = connSkt.recv(100)
        print '[+] %d/tcp open' % tgtPort
        print '[+] ' + str(res)
        connSkt.close()
    except:
        print '[-] %d/tcp closed' % tgtPort

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print '[-] Cannot resolve \'%s\': Unknown host ' % tgtHost
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print '\n[+] Scan results for: ' + tgtName[0]
    except:
        print '\n[+] Scan results for: ' + tgtIP

    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print 'Scanning port ' + tgtPort
        connScan(tgtHost, int(tgtPort))

# basic options parsing which will be common
def main():
    parser = optparse.OptionParser("Usage: tcpportscanner.py -H <target host> -p <target port>")
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPorts', type='string', help='specify target port')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = options.tgtPorts
    if (tgtHost == None) | (tgtPorts == None):
        print parser.usage
        exit(0)
    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()