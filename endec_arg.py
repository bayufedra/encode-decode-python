#!/bin/env python
import re
import base64
import hashlib
import binascii
import argparse
from sys import argv
from itertools import cycle
from string import lowercase, uppercase

author = '''
   =====================================================
    ===================================================
       =-=-=-=-=-=-=-=- B3yeZ Tools -=-=-=-=-=-=-=-=
      =-=-=-=-=-=- Author : Bayu Fedra A -=-=-=-=-=-=
    ===================================================
   =====================================================
    ____                  ______  _______          _
   |  _ \\                |___  / |__   __|        | |
   | |_) | ___ _   _  ___   / /     | | ___   ___ | |___
   |  _ < / _ \\ | | |/ _ \\ / /      | |/ _ \\ / _ \\| / __|
   | |_) |  __/ |_| |  __// /__     | | (_) | (_) | \\__ \\
   |____/ \\___|\\__, |\\___/_____|    |_|\\___/ \\___/|_|___/
                __/ |
               |___/            bayufedraaxtkja@gmail.com
'''
b3yez = '{+} Thank You dude, please keep support, FB : https://www.facebook.com/bayufedra / Instagram : http://instagram.com/bayufedraa {+}'


def fn_result(s_res):
    print '[+] Result => {}'.format(s_res)
    #print b3yez

def fn_error(s_msg):
    print '[-] Error, not {} strings'.format(s_msg)

def fn_main():
    print author
    halah = argparse.ArgumentParser(description=' [+] Tools to Encoding, Decoding and Hashing [+]')
    halah.add_argument('str', help='Strings')
    halah.add_argument('-e', action='store_true', help='encode strings')
    halah.add_argument('-d', action='store_true', help='decode strings')
    halah.add_argument('-brute', action='store_true', help='Bruteforce char')
    halah.add_argument('-key', type=int, action='store', help='Key for char caessar cipher')
    halah.add_argument('-k', type=str, action='store', help='Key for char xor')
    halah.add_argument('-b64', action='store_true', help='Base64 encryptions')
    halah.add_argument('-b32', action='store_true', help='Base32 encryptions')
    halah.add_argument('-b16', action='store_true', help='Base16 encryptions')
    halah.add_argument('-hex', action='store_true', help='Hexadecimal')
    halah.add_argument('-dec', action='store_true', help='Decimal')
    halah.add_argument('-bin', action='store_true', help='Binary')
    halah.add_argument('-rev', action='store_true', help='Reverse Strings')
    halah.add_argument('-rot13', action='store_true', help='ROT 13 Cipher')
    halah.add_argument('-caes', action='store_true', help='Caessar Cipher')
    halah.add_argument('-xor', action='store_true', help='XOR Cipher')
    halah.add_argument('-md5', action='store_true', help='MD5 Hashing')
    halah.add_argument('-sha1', action='store_true', help='SHA1 Hashing')
    halah.add_argument('-sha256', action='store_true', help='SHA256 Hashing')
    halah.add_argument('-sha512', action='store_true', help='SHA512 Hashing')
    wibu = halah.parse_args()

    if wibu.b64 and wibu.e:
        fn_result(base64.b64encode(wibu.str))

    if wibu.b64 and wibu.d:
        try:
            fn_result(base64.b64decode(wibu.str))
        except:
            fn_error('base64')

    if wibu.b32 and wibu.e:
        fn_result(base64.b32encode(wibu.str))

    if wibu.b32 and wibu.d:
        try:
            fn_result(base64.b32decode(wibu.str))
        except:
            fn_error('base32')

    if wibu.b16 and wibu.e:
        fn_result(base64.b16encode(wibu.str))

    if wibu.b16 and wibu.d:
        try:
            fn_result(base64.b16decode(wibu.str))
        except:
            fn_error('base16')

    if wibu.hex and wibu.e:
        fn_result(binascii.hexlify(wibu.str))

    if wibu.hex and wibu.d:
        try:
            fn_result(binascii.unhexlify(wibu.str))
        except:
            fn_error('hexadecimal')

    if wibu.dec and wibu.e:
        fn_result(''.join([str(ord(c)) for c in wibu.str]))

    if wibu.dec and wibu.d:
        try:
            fn_result(re.sub('1?..', lambda m: chr(int(m.group())), wibu.str))
        except:
            fn_error('decimal')

    if wibu.bin and wibu.e:
        fn_result(bin(int(binascii.hexlify(wibu.str), 16)))

    if wibu.bin and wibu.d:
        try:
            fn_result(binascii.unhexlify('%x' % int(wibu.str, 2)))
        except:
            fn_error('binary')

    if wibu.rev:
        fn_result(wibu.str[::-1])

    if wibu.rot13:
        if wibu.rot13 or wibu.e or wibu.d:
            fn_result(wibu.str.encode('rot_13'))

    if wibu.caes and wibu.key:
        en = wibu.str
        n = wibu.key
        hasil = ''
        for x in range(len(en)):
            if en[x].isalpha():
                if en[x].islower():
                    hasil = hasil + lowercase[(lowercase.find(en[x]) + n) % 26]
                else:
                    hasil = hasil + uppercase[(uppercase.find(en[x]) + n) % 26]
            else:
                hasil = hasil + en[x]
        fn_result(hasil)

    if wibu.caes and wibu.brute:
        for i in range(26):
            hasil = ''
            for x in range(len(wibu.str)):
                if wibu.str[x].isalpha():
                    if wibu.str[x].islower():
                        hasil = hasil + lowercase[(lowercase.find(wibu.str[x]) + i) % 26]
                    else:
                        hasil = hasil + uppercase[(uppercase.find(wibu.str[x]) + i) % 26]
                else:
                    hasil = hasil + wibu.str[x]
            print '{} => [+] Result => {}'.format(str(i), hasil)

    if wibu.xor and wibu.brute:
        for i in range(256):
            print '{} => [+] Result => {}'.format(str(i), ''.join([chr(ord(l) ^ i) for l in wibu.str]))

    if wibu.xor and wibu.k:
        string = wibu.str
        n = wibu.k
        hasil = ''
        for c, k in zip(string, cycle(n)):
            hasil += chr(ord(c) ^ ord(k))
        fn_result(hasil)

    if wibu.md5:
        if wibu.md5 or wibu.e:
            fn_result(hashlib.md5(wibu.str.encode('utf')).hexdigest())

    if wibu.sha1:
        if wibu.sha1 or wibu.e:
            fn_result(hashlib.sha1(wibu.str.encode('utf')).hexdigest())

    if wibu.sha256:
        if wibu.sha256 or wibu.e:
            fn_result(hashlib.sha256(wibu.str.encode('utf')).hexdigest())

    if wibu.sha512:
        if wibu.sha512 or wibu.e:
            fn_result(hashlib.sha512(wibu.str.encode('utf')).hexdigest())


if __name__ == '__main__':
    fn_main()
