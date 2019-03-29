#!/usr/bin/env python
R = '\x1b[31;1m'
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
a = '\x1b]31;1m'
from os import *
from time import sleep
import sys, re, random, time, unittest
from urllib2 import *
from time import sleep
try:
    from main import *
except ImportError:
    print '\n[-] WebKiller Error'
    quit()

reload(sys)
sys.setdefaultencoding('utf-8')

def versionPy():
    version = python_version().startswith('3', 0, len(python_version()))
    if version:
        print ('Are you using python version {}\nPlease, use version 2.X of python').format(python_version())
        exit()


def banner():
    print "\n\x1b[31;1m  _    _        _     \x1b[36;1m _   __ _  _  _\n\x1b[31;1m | |  | |      | |    \x1b[36;1m| | / /(_)| || |\n\x1b[31;1m | |  | |  ___ | |__  \x1b[36;1m| |/ /  _ | || |  ___  _ __\n\x1b[31;1m | |/\\| | / _ \\| '_ \\ \x1b[36;1m|    \\ | || || | / _ \\| '__|\n\x1b[31;1m \\  /\\  /|  __/| |_) |\x1b[36;1m| |\\  \\| || || ||  __/| |\n\x1b[31;1m  \\/  \\/  \\___||_.__/ \x1b[36;1m\\_| \\_/|_||_||_| \\___||_|\n"


def inf1():
    print '  \x1b[31;1m+------===[ \x1b[36;1mAuthor   \xc2\xbb \x1b[37;1mGunadiCBR \x1b[31;1m]===------+'


def inf2():
    print '  \x1b[31;1m+------===[ \x1b[36;1mPlatform \xc2\xbb \x1b[37;1mpython2.7 \x1b[31;1m]===------+'


def inf3():
    print '  \x1b[31;1m+------===[ \x1b[36;1mVersion  \xc2\xbb \x1b[37;1m1.5       \x1b[31;1m]===------+'


def Kembali():
    print ' '
    try:
        bk = raw_input('\x1b[31;1m[*] \x1b[36;1mBack\x1b[32;1m(b) \x1b[36;1mor Exit\x1b[32;1m(e) \x1b[37;1m--> \x1b[37;0m')
    except:
        Kembali()

    if bk == 'b':
        main()
    else:
        if bk == 'e':
            print ' '
            print '\x1b[31;1m[\x1b[33;1m-\x1b[31;1m] Exiting'
            sleep(2)
            quit()
        else:
            print ' '
            print 'something went wrong'
            sleep(0.5)
            Kembali()


def l():
    print ' '


def clear():
    os.system('clear')


def clear1():
    if sys.platform == 'linux2':
        clear()
    else:
        if sys.platform == 'termux':
            clear()
        else:
            if sys.platform == 'win32':
                clear()
            else:
                clear()


def queue():
    print '\n\x1b[31;1m[\x1b[33;1m01\x1b[31;1m] > \x1b[37;0mWho Is Lookup\n\x1b[31;1m[\x1b[33;1m02\x1b[31;1m] > \x1b[37;0mDNS Lookup + Cloudflare Detector\n\x1b[31;1m[\x1b[33;1m03\x1b[31;1m] > \x1b[37;0mIP Scan\n\x1b[31;1m[\x1b[33;1m04\x1b[31;1m] > \x1b[37;0mPort Scan\n\x1b[31;1m[\x1b[33;1m05\x1b[31;1m] > \x1b[37;0mHTTP Header Grabber\n\x1b[31;1m[\x1b[33;1m06\x1b[31;1m] > \x1b[37;0mHoneypot Detector\n\x1b[31;1m[\x1b[33;1m07\x1b[31;1m] > \x1b[37;0mLink Grabber\n\x1b[31;1m[\x1b[33;1m08\x1b[31;1m] > \x1b[37;0mRobots.txt Scanner\n\x1b[31;1m[\x1b[33;1m09\x1b[31;1m] > \x1b[37;0mZone Transfer\n\x1b[31;1m[\x1b[33;1m10\x1b[31;1m] > \x1b[37;0mIP Location Finder\n\x1b[31;1m[\x1b[33;1m11\x1b[31;1m] > \x1b[37;0mTraceRoute\n\x1b[31;1m[\x1b[33;1m12\x1b[31;1m] > \x1b[37;0mSubnet Lookup\n\x1b[31;1m[\x1b[33;1m13\x1b[31;1m] > \x1b[37;0mExatrac Links\n\x1b[31;1m[\x1b[33;1m14\x1b[31;1m] > \x1b[37;0mHost DNS Finder\n\x1b[31;1m[\x1b[33;1m15\x1b[31;1m] > \x1b[37;0mReverse DNS Lookup\n\x1b[31;1m[\x1b[33;1m16\x1b[31;1m] > \x1b[37;0mHost Finder\n\x1b[31;1m[\x1b[33;1m17\x1b[31;1m] > \x1b[37;0mReverse IP Lookup\n\x1b[31;1m[\x1b[33;1m18\x1b[31;1m] > \x1b[37;0mHTTP Header\n\x1b[31;1m[\x1b[33;1m18\x1b[31;1m] > \x1b[37;0mGeoIp Lookup\n\x1b[31;1m[\x1b[33;1m20\x1b[31;1m] > \x1b[37;0mAS Lookup\n\x1b[31;1m[\x1b[33;1m21\x1b[31;1m] > \x1b[37;0mFind DNS Host Records\n\x1b[31;1m[\x1b[33;1m22\x1b[31;1m] > \x1b[37;0mFind Shared DNS Server\n\x1b[31;1m[\x1b[33;1m23\x1b[31;1m] > \x1b[37;0mSubnet Calculator\n\x1b[31;1m[\x1b[33;1m24\x1b[31;1m] > \x1b[37;0mPing\n\x1b[31;1m[\x1b[33;1mAB\x1b[31;1m] > \x1b[37;0mAbout Us\n\x1b[31;1m[\x1b[33;1m00\x1b[31;1m] > \x1b[37;0mExit\n'


def main():
    clear1()
    banner()
    inf1()
    inf2()
    inf3()
    queue()
    try:
        cmd = raw_input('\x1b[31;1m[\x1b[33.*\x1b[31;1m] \x1b[37;0mWebkiller \x1b[37;1m--> \x1b[33;1m')
    except:
        quit()

    if cmd == '1' or cmd == '01':
        l()
        whs()
    else:
        if cmd == '2' or cmd == '02':
            l()
            dnslookup()
        else:
            if cmd == '3' or cmd == '03':
                l()
                meko()
            else:
                if cmd == '4' or cmd == '04':
                    l()
                    portscan()
                else:
                    if cmd == '5' or cmd == '05':
                        l()
                        hhg()
                    else:
                        if cmd == '6' or cmd == '06':
                            l()
                            honeypotdetector()
                        else:
                            if cmd == '7' or cmd == '07':
                                l()
                                grabber()
                            else:
                                if cmd == '8' or cmd == '08':
                                    l()
                                    rts()
                                else:
                                    if cmd == '9' or cmd == '09':
                                        l()
                                        zonet()
                                    else:
                                        if cmd == '10':
                                            l()
                                            iplocationfinder()
                                            Kembali()
                                        else:
                                            if cmd == '11':
                                                l()
                                                traceroute()
                                            else:
                                                if cmd == '12':
                                                    l()
                                                    subnetlookup()
                                                else:
                                                    if cmd == '13':
                                                        l()
                                                        exactraclinks()
                                                    else:
                                                        if cmd == '14':
                                                            l()
                                                            hostdnsfinder()
                                                        else:
                                                            if cmd == '15':
                                                                l()
                                                                reversedns()
                                                            else:
                                                                if cmd == '16':
                                                                    l()
                                                                    hostfinder()
                                                                else:
                                                                    if cmd == '17':
                                                                        l()
                                                                        reverseiplookup()
                                                                    else:
                                                                        if cmd == '18':
                                                                            l()
                                                                            httpheader()
                                                                        else:
                                                                            if cmd == '19':
                                                                                l()
                                                                                geoiplookup()
                                                                            else:
                                                                                if cmd == '20':
                                                                                    l()
                                                                                    aslookup()
                                                                                else:
                                                                                    if cmd == '21':
                                                                                        l()
                                                                                        finddnshostrecords()
                                                                                    else:
                                                                                        if cmd == '22':
                                                                                            l()
                                                                                            findshareddnsservers()
                                                                                        else:
                                                                                            if cmd == '23':
                                                                                                l()
                                                                                                sucal()
                                                                                            else:
                                                                                                if cmd == '24':
                                                                                                    l()
                                                                                                    ping()
                                                                                                else:
                                                                                                    if cmd == 'AB' or cmd == 'ab':
                                                                                                        clear()
                                                                                                        banner()
                                                                                                        abouttentang()
                                                                                                        Kembali()
                                                                                                    else:
                                                                                                        if cmd == '00' or cmd == '0':
                                                                                                            print ' '
                                                                                                            print '\x1b[31;1m[\x1b[33;1m*\x1b[31;1m] \x1b[37;1mExiting Program ...'
                                                                                                            sleep(1)
                                                                                                            print '\x1b[31;1m[\x1b[33;1m*\x1b[31;1m] \x1b[37;1mHave Bad Day ...'
                                                                                                            sleep(1.5)
                                                                                                            print ' '
                                                                                                            quit()
                                                                                                        else:
                                                                                                            main()


main()
