#!/usr/bin/env python
H = '\x1b[95m'
B = '\x1b[94m'
G = '\x1b[92m'
W = '\x1b[93m'
F = '\x1b[91m'
E = '\x1b[0m'
U = '\x1b[4m'
O = '\x1b[33m'
LL = '\x1b[1;38;5;228m'
HB = '\x1b[1;38;5;32m'
RR = '\x1b[1;38;5;225m'
ll = '\x1b[1 38;5;223'
R = '\x1b[31;1m'
a = '\x1b[31;1m'
b = '\x1b]33;1m'
c = '\x1b[36;1m'
d = '\x1b[37;1m'
from os import *
from time import sleep
import os, sys, random, time, unittest
from urllib2 import *
reload(sys)
sys.setdefaultencoding('utf-8')

def Banner():
    info = '\x1b[31m\n+------===[ Author   \xc2\xbb GunadiCBR ]===------+\n +-----===[ Version  \xc2\xbb 1.5       ]===-----+\n  +----===[ Platform \xc2\xbb python2.7 ]===----+\n\t'


def cls():
    os.system('clear')


def dick():
    cls()
    Banner()
    slow('\x1b[33m[*] \x1b[32mThanks For Using My Tool')
    slow('\x1b[33m[*] \x1b[32mHave A Nice Day ...')
    slow('\x1b[33m[*] \x1b[32mGood By ...')
    key = input(' ')
    quit()


def clear():
    os.system('clear')


def Kembali():
    print ' '
    try:
        bk = input('\x1b[31;1m[*] \x1b[36;1mBack\x1b[32;1m(b) \x1b[36;1mor Exit\x1b[32;1m(e) \x1b[37;1m--> \x1b[37;0m')
    except:
        Kembali()

    if bk == 'b':
        print ' '
        os.system('python2 run.py')
    else:
        if bk == 'e':
            os.system('clear')
            dick()
            sleep(2)
            exit()
        else:
            print ' '
            print 'something went wrong'
            sleep(0.5)
            Kembali()


def Exit():
    print ' '
    try:
        ex = input('\x1b[31;1m[*] \x1b[37;0mDo You Want To Exit \x1b[31;1m[\x1b[33;1my\x1b[37;0m/\x1b[33;1mn\x1b[31;1m] \x1b[37;1m--> \x1b[31;1m')
    except:
        Exit()

    if ex == 'y':
        os.system('clear')
        print '\n\x1b[33m[*] \x1b[32mThanks For Using My Tool\n\x1b[33m[*] \x1b[32mGood By'
        sleep(1)
        sys.exit()
    else:
        if ex == 'n':
            os.system('clear')
        else:
            print ' '
            print 'something went wrong'
            sleep(0.5)
            Exit()


def Ulang():
    print '\x1b[33;1m[\x1b[31;1m!\x1b[33;1m] \x1b[31;1mERROR : \x1b[37;0mWrong Input \x1b[31;1m!!!'
    sleep(1)


def ulang():
    python = sys.executable
    os.execl(python, python, *sys.argv)
    curdir = os.getcwd()


def info0():
    print HB + 'Author   \x1b[31;1m\xc2\xbb \x1b[33mGunadiCBR\n\x1b[1;38;5;32mVersion  \x1b[31;1m\xc2\xbb \x1b[33m1.5\n\x1b[1;38;5;32mPlatform \x1b[31;1m\xc2\xbb \x1b[33mpython2.7'


def abouttentang():
    print HB + '\nAuthor   \x1b[31;1m\xc2\xbb \x1b[33mGunadiCBR\n\x1b[1;38;5;32mVersion  \x1b[31;1m\xc2\xbb \x1b[33mv1.5\n\x1b[1;38;5;32mPlatform \x1b[31;1m\xc2\xbb \x1b[33mpython2.7\n\x1b[1;38;5;32mgithub   \x1b[31;1m\xc2\xbb \x1b[33mhttps://github.com/afelfgie\n\x1b[1;38;5;32mContack Me \x1b[31;1m:\x1b[36m\n*) \x1b[1;38;5;225mPhone  : 6285341899229\x1b[36m\n*) \x1b[1;38;5;225mFb     : https://fb.com/unknown\x1b[36m\n*) \x1b[1;38;5;225mE-mail : iamcbr26099@gmail.com\x1b[36m\n\n\x1b[31m[*] \x1b[37;1mWebKiller Is an all is one basic information\ngathering and vulnerability assessment tool'


def sucal():
    try:
        domip = raw_input('[*] Enter Domain Or Ip: ')
    except:
        os.system('python2 run.py')

    scl = 'http://api.hackertarget.com/subnetcalc/?q=' + domip
    sll = urlopen(scl).read()
    print sll


def hpd():
    ip = raw_input('[*] Enter Ip: ')
    honey = 'https://api.shodan.io/labs/honeyscore/' + ip + '?key=C23OXE0bVMrul2YeqcL7zxb6jZ4pj2by'
    try:
        phoney = fetch(honey)
    except URLError:
        phoney = None
        write(var='@', color=r, data='Sorry, The webserver of the website you entered have no domains other then the one you gave ')

    if phoney:
        print ('Honeypot Percent : {probability}').format(color='2' if float(phoney) < 0.5 else '3', probability=float(phoney) * 10)
        print '\n'
    return


def ping():
    try:
        domip = raw_input('[*] Enter Domain Or Ip Address: ')
    except:
        quit()

    port = 'http://api.hackertarget.com/nping/?q=' + domip
    pport = urlopen(port).read()
    print pport


def reverseiplookup():
    try:
        domip = raw_input('[*] Enter Domain Or Ip: ')
    except:
        quit()

    ril = 'http://api.hackertarget.com/reverseiplookup/?q=' + domip
    rril = urlopen(ril).read()
    print rril


def httpheader():
    try:
        domip = raw_input('[*] Enter Domain Or IP: ')
    except:
        httpheader()

    hdr = 'https://api.hackertarget.com/httpheaders/?q=' + domip
    hhdr = urlopen(hdr).read()
    print hhdr
    Kembali()


def geoiplookup():
    try:
        ip = raw_input('[*] Enter Ip: ')
    except:
        geoiplookup()

    gil = 'https://api.hackertarget.com/geoip/?q=' + ip
    ggil = urlopen(gil).read()
    print ggil
    Kembali()


def aslookup():
    try:
        ip = raw_input('Enter Ip: ')
    except:
        aslookup()

    al = 'https://api.hackertarget.com/aslookup/?q=' + ip
    aal = urlopen(al).read()
    print aal
    Kembali()


def finddnshostrecords():
    try:
        domip = raw_input('[*] Enter Domain Or Ip: ')
    except:
        quit()

    fdhr = 'https://api.hackertarget.com/hostsearch/?q=' + domip
    ffdhr = urlopen(fdhr).read()
    print ffdhr
    Kembali()


def findshareddnsservers():
    try:
        domip = raw_input('[*] Enter Domain Or Ip: ')
    except:
        quit()

    ys = 'https://api.hackertarget.com/findshareddns/?q=' + domip
    yys = urlopen(ys).read()
    print yys
    Kembali()


def whs():
    try:
        domip = raw_input('[*] Enter Domain Or Ip: ')
    except:
        whs()

    whs = 'http://api.hackertarget.com/whois/?q=' + domip
    pwhs = urlopen(whs).read()
    print pwhs
    Kembali()


def uph():
    try:
        memek = raw_input('Press Enter To Continue')
    except:
        uph()

    meko()


def meko():
    while True:
        print 'MEMEK <> KONTOL'
        sleep(0.1)


def zonet():
    try:
        domain = raw_input('\x1b[34m[*] \x1b[33mEnter Domain: \x1b[32m')
    except:
        zonet()
    else:
        zone = 'http://api.hackertarget.com/zonetransfer/?q=' + domain
        try:
            domain = raw_input('\x1b[31m[*] \x1b[33mEnter Domain: \x1b[32m')
            pzone = urlopen(zone).read()
            print pzone
            Kembali()
        except 'failed' in pzone:
            print '\x1b[31m[-] \x1b[37;0mZone transfer failed'
            Kembali()


def portscan():
    try:
        domip = raw_input('\x1b[34m[*] \x1b[33mEnter Domain Or Ip: \x1b[32m')
    except:
        portscan()

    port = 'http://api.hackertarget.com/nmap/?q=' + domip
    pport = urlopen(port).read()
    print pport
    Kembali()


def hhg():
    try:
        domip = raw_input('\x1b[34m[*] \x1b[33mEnter Domain Or Ip: ')
    except:
        hhg()

    header = 'http://api.hackertarget.com/httpheaders/?q=' + domip
    pheader = urlopen(header).read()
    print pheader
    Kembali()


def dnslookup():
    try:
        domain = raw_input('\x1b[31m[*] \x1b[33mEnter Domain: \x1b[32m')
    except:
        dnslookup()

    ns = 'http://api.hackertarget.com/dnslookup/?q=' + domain
    pns = urlopen(ns).read()
    print pns
    if 'cloudflare' in pns:
        print '\x1b[31m[+] \x1b[37;0mCloudflare Detected !'
        sleep(2)
        Kembali()
    else:
        print '\x1b[31m[-] \x1b[37;0mNot Protected By cloudflare'
        sleep(2)
        Kembali()


def honeypotdetector():
    try:
        ip = raw_input('\x1b[34m[*] \x1b[33mEnter IP Address: \x1b[37;0m')
    except:
        honeypotdetector()

    honey = 'https://api.shodan.io/labs/honeyscore/' + ip + '?key=C23OXE0bVMrul2YeqcL7zxb6jZ4pj2by'
    phoney = urlopen(honey).read()
    if '0.0' in phoney:
        print '\x1b[1;32mHoneypot Probabilty: 0%\x1b[1;m'
    if '0.1' in phoney:
        print '\x1b[1;32mHoneypot Probabilty: 10%\x1b[1;m'
    if '0.2' in phoney:
        print '\x1b[1;32mHoneypot Probabilty: 20%\x1b[1;m'
    if '0.3' in phoney:
        print '\x1b[1;32mHoneypot Probabilty: 30%\x1b[1;m'
    if '0.4' in phoney:
        print '\x1b[1;32mHoneypot Probabilty: 40%\x1b[1;m'
    if '0.5' in phoney:
        print '\x1b[1;31mHoneypot Probabilty: 50%\x1b[1;m'
    if '0.6' in phoney:
        print '\x1b[1;31mHoneypot Probabilty: 60%\x1b[1;m'
    if '0.7' in phoney:
        print '\x1b[1;31mHoneypot Probabilty: 70%\x1b[1;m'
    if '0.8' in phoney:
        print '\x1b[1;31mHoneypot Probabilty: 80%\x1b[1;m'
    if '0.9' in phoney:
        print '\x1b[1;31mHoneypot Probabilty: 90%\x1b[1;m'
    if '1.0' in phoney:
        print '\x1b[1;31mHoneypot Probabilty: 100%\x1b[1;m'


def rts():
    try:
        domain = raw_input('\x1b[34m[*] \x1b[33mEnter Domain: \x1b[32m')
    except:
        rts()

    if 'http://' in domain or 'https://' in domain:
        pass
    else:
        domain = 'http://' + domain
    robot = domain + '/robots.txt'
    probot = urlopen(robot).read()
    print probot


def grabber():
    try:
        page = raw_input('\x1b[34m[*] \x1b[33mEnter URL: \x1b[32m')
    except:
        grabber()

    if 'http://' in page or 'https://' in page or 'www' in page:
        pass
    else:
        page = 'http://' + page
    crawl = 'https://api.hackertarget.com/pagelinks/?q=' + page
    pcrawl = urlopen(crawl).read()
    print pcrawl


def iplocationfinder():
    try:
        ip = raw_input('\x1b[31;1m[*] Enter Ip: ')
    except:
        iplocationfinder()

    geo = 'http://ipinfo.io/' + ip + '/geo'
    pgeo = urlopen(geo).read()
    print pgeo


def traceroute():
    try:
        domip = raw_input('[*] Enter Domain Or Ip: ')
    except:
        traceroute()

    trace = 'https://api.hackertarget.com/mtr/?q=' + domip
    ptrace = urlopen(trace).read()
    print ptrace


def subnetlookup():
    try:
        ip = raw_input('[*] Enter Ip: ')
    except:
        subnetlookup()

    subnet = 'https://api.hackertarget.com/subnetcalc/?q=' + ip
    psubnet = urlopen(subnet).read()
    print psubnet


def exactraclinks():
    try:
        dom = raw_input('[*] Enter Domain: ')
    except:
        exactraclinks()

    exac = 'https://api.hackertarget.com/pagelinks/?q=' + dom
    pexac = urlopen(exac).read()
    print pexac


def hostdnsfinder():
    try:
        dom = raw_input('[*] Enter Domain: ')
    except:
        hostdnsfinder()

    host = 'https://api.hackertarget.com/mtr/?q=' + dom
    hhost = urlopen(host).read()
    print hhost


def reversedns():
    try:
        dom = raw_input('[*] Enter Domain: ')
    except:
        reversedns()

    dns = 'http://api.hackertarget.com/reverseiplookup/?q=' + dom
    ddns = urlopen(dns).read()
    print ddns


def hostfinder():
    try:
        dom = raw_input('[*] Enter Domain: ')
    except:
        hostfinder()

    host = 'http://api.hackertarget.com/hostsearch/?q=' + dom
    hhost = urlopen(host).read()
    print hhost


def info():
    print HB + 'Author   \x1b[31;1m\xc2\xbb \x1b[33mGunadiCBR\n\x1b[1;38;5;32mVersion  \x1b[31;1m\xc2\xbb \x1b[33m1.2\n\x1b[1;38;5;32mPlatform \x1b[31;1m\xc2\xbb \x1b[33mpython2.7'


def about():
    os.system('clear')
    print HB + '\nAuthor   \x1b[31;1m\xc2\xbb \x1b[33mGunadiCBR\n\x1b[1;38;5;32mVersion  \x1b[31;1m\xc2\xbb \x1b[33mv2.0\n\x1b[1;38;5;32mPlatform \x1b[31;1m\xc2\xbb \x1b[33mpython2.7\n\x1b[1;38;5;32mgithub   \x1b[31;1m\xc2\xbb \x1b[33mhttps://github.com/afelfgie\n\x1b[1;38;5;32mContack Me \x1b[31;1m:\x1b[36m\n*) \x1b[1;38;5;225mPhone  : 6285341899229\x1b[36m\n*) \x1b[1;38;5;225mFb     : https://fb.com/unknown\x1b[36m\n*) \x1b[1;38;5;225mE-mail : gunadirenta@gmail.com\n'
