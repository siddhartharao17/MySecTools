
# Password cracker using Crypt module and dictionary
# Author: Sid

import sys
import crypt

def crackPass(cryptPasswd):
    salt = cryptPasswd[0:2]
    dictionaryFile = sys.argv[2]
    dictionaryFileP = open(dictionaryFile, "r")
    for word in dictionaryFileP.readlines():
        word = word.strip('\n')
        # print 'trying word: %s' % (word)
        if cryptPasswd == crypt.crypt(word, salt):
            print "[+] Password cracked and found: %s \n" % str(word)
            return
    print "[-] Sorry! Password could not be cracked.\n"
    return

def main():
    if len(sys.argv) == 3:
        # print 'Number of arg: %s' % len(sys.argv)
        cryptPassFilename = sys.argv[1]
        cryptPassFileP = open(cryptPassFilename,"r")
        for entry in cryptPassFileP.readlines():
            user = entry.split(':')[0]
            cryptPasswd = entry.split(':')[1].strip(' ')
            # salt = cryptPasswd[0:2]
            print "[+] Cracking password for user: %s" % str(user)
            crackPass(cryptPasswd)
    else:
        print "[-] Usage: python passwdcraker.py <encrypted passwd file> <dictionary file>"
        exit(0)

if __name__ == "__main__":
    main()