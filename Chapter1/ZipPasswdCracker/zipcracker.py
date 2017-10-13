import sys
import zipfile
import optparse #used to parse flags and optional parameters
from threading import Thread

def extractFile(zFile, passwd):
    try:
        zFile.extractall(pwd=passwd)
        print '[+] Password Cracked: %s' % (passwd)
    # except Exception, e:
    except:
        pass

def main():
    parser = optparse.OptionParser("Usage: zipcracker.py -f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
    (options, args) = parser.parse_args()
    print (options, args)
    if (options.zname == None) | (options.dname == None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)

    for item in passFile.readlines():
        passwd = item.strip('\n')
        t = Thread(target=extractFile, args=(zFile, passwd))
        t.start()


if __name__ == '__main__':
    main()