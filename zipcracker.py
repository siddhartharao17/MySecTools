import zipfile
from threading import Thread

def extractFunc(zFile, passwd):
    try:
        zFile.extractall(pwd=passwd)
        print '[+] Password Cracked: %s' % (passwd)
    # except Exception, e:
    except:
        pass

def main():
    zFile = zipfile.ZipFile('evil.zip')
    passFile = open('dictionary.txt')

    for item in passFile.readlines():
        passwd = item.strip('\n')
        t = Thread(target=extractFunc, args=(zFile, passwd))
        t.start()
        # found = extractFunc(zFile, passwd)
        # if found:
        #     print '[+] Password Cracked: %s' % (found)

if __name__ == '__main__':
    main()