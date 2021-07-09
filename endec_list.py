#!/bin/env python
import os
import re
import sys
import base64
import hashlib
import binascii
import platform
import itertools
from itertools import cycle
from string import lowercase, uppercase

str_menu = '''
 [1] Base64
 [2] Base32
 [3] Base16
 [4] Binary
 [5] Hexadecimal
 [6] Decimal
 [7] ROT13
 [8] Caesar
 [9] Reversed Text
[10] MD5 Hash
[11] SHA1 Hash
[12] SHA256 Hash
[13] SHA512 Hash
[14] Xor Bruteforce
[15] Xor With Key
[16] Cancel

[i] Pilihan : '''

str_endeop = '''
[1] Encode
[2] Decode

[i] Opsi : '''

str_cont = '''
[1] Lanjut
[2] Tidak

[i] Pilihan: '''

l_edr = ['[+] Hasil : ',\
         '[i] Text to Encode : ',\
         '[i] Text to Decode : ']

def fn_x64(i_opt):
    a = [{1:base64.b64encode, 2:base64.b64decode},\
         {1:base64.b32encode, 2:base64.b32decode},\
         {1:base64.b16encode, 2:base64.b16decode}]
    b = int(raw_input(str_endeop))
    print ''
    if (b > 2): sys.exit()
    s = raw_input(l_edr[b])
    print l_edr[0] + a[i_opt][b](s)

def fn_hex():
    a = int(raw_input(str_endeop))
    print ''
    if (a > 2): sys.exit()
    b = raw_input(l_edr[a])
    return a,b

def fn_csr(n, s_csr):
    s_out = ''
    for x in xrange(len(s_csr)):
        if s_csr[x].isalpha():
            if s_csr[x].islower():
                s_out += lowercase[(lowercase.find(s_csr[x]) + n) % 26]
            else:
                s_out += uppercase[(uppercase.find(s_csr[x]) + n) % 26]
        else:
            s_out += s_csr[x]
    return s_out

def fn_hash(i_opt):
    a = [{0:hashlib.md5, 1:'[i] MD5 Hash Encode: '},\
         {0:hashlib.sha1, 1:'[i] SHA1 Hash Encode: '},\
         {0:hashlib.sha256, 1:'[i] SHA256 Hash Encode: '},\
         {0:hashlib.sha512, 1:'[i] SHA512 Hash Encode: '}]
    print l_edr[0] + a[i_opt][0](raw_input(a[i_opt][1]).encode('utf')).hexdigest()

def fn_done():
    print '''
[+] Thank You dude, please keep support
[+] FB : https://www.facebook.com/bayufedra
[+] Instagram : http://instagram.com/bayufedraa'''
    sys.exit()

def fn_main():
    if platform.system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

    print '''
        ===================================================
         =================================================
            =-=-=-=-=-=-=-= B3yeZ Tools =-=-=-=-=-=-=-=
           =-=-=-=-=-= Author : Bayu Fedra A =-=-=-=-=-=
         =================================================
        ===================================================
        ____                  ______  _______          _
       |  _ \\                |___  / |__   __|        | |
       | |_) | ___ _   _  ___   / /     | | ___   ___ | |___
       |  _ < / _ \\ | | |/ _ \\ / /      | |/ _ \\ / _ \\| / __|
       | |_) |  __/ |_| |  __// /__     | | (_) | (_) | \\__ \\
       |____/ \\___|\\__, |\\___/_____|    |_|\\___/ \\___/|_|___/
                    __/ |
                   |___/            bayufedraaxtkja@gmail.com

        root@B3yeZ:~# cat list.txt'''

    while True:
        try:
            listt = int(raw_input(str_menu))
            if listt == 1:
                fn_x64(0)

            elif listt == 2:
                fn_x64(1)

            elif listt == 3:
                fn_x64(2)

            elif listt == 4:
                o,s = fn_hex()
                print '{}{}'.format(l_edr[0], bin(int(binascii.hexlify(s), 16)) if (o == 1) else binascii.unhexlify('%x' % int(s, 2)) if (o == 2) else '')

            elif listt == 5:
                o,s = fn_hex()
                print '{}{}'.format(l_edr[0], binascii.hexlify(s) if (o == 1) else binascii.unhexlify(s) if (o == 2) else '')

            elif listt == 6:
                o = int(raw_input(str_endeop))
                print ''
                if (o > 2): break
                s = raw_input(l_edr[o])
                print '{}{}'.format(l_edr[0], ''.join([str(ord(c)) for c in s]) if (o == 1) else re.sub('1?..', lambda m: chr(int(m.group())), s) if (o == 2) else '')

            elif listt == 7:
                print '{}{}'.format(l_edr[0], raw_input('[i] Text to En/Decode : ').encode('rot_13'))

            elif listt == 8:
                o = int(raw_input(str_endeop))
                print ''
                if o == 1:
                    en = raw_input(l_edr[o])
                    n = input('[i] Key : ')
                    print '{}{}'.format(l_edr[0], fn_csr(n, en))
                if o == 2:
                    en = raw_input('[i] Caesar to Bruteforce : ')
                    for i in xrange(26):
                        print '  {} => Hasil ===> {}'.format(str(i), fn_csr(i, en))

            elif listt == 9:
                print '{}{}'.format(l_edr[0], raw_input('[i] Text to Reverse : ')[::-1])

            elif listt == 10:
                fn_hash(0)

            elif listt == 11:
                fn_hash(1)

            elif listt == 12:
                fn_hash(2)

            elif listt == 13:
                fn_hash(3)

            elif listt == 14:
                a = raw_input('[i] XOR to Bruteforce : ')
                for i in xrange(256):
                    print '{} => Hasil ===> {}'.format(str(i), ''.join([chr(ord(l) ^ i) for l in a]))

            elif listt == 15:
                a = raw_input('[i] Strings to XOR : ')
                b = raw_input('[i] Key : ')
                hasil = ''
                for c, k in zip(a, cycle(b)):
                    hasil += chr(ord(c) ^ ord(k))
                print '{}{}'.format(l_edr[0], hasil)

            elif listt == 16:
                fn_done()

            if int(raw_input(str_cont)) == 2:
                fn_done()

        except KeyboardInterrupt:
                sys.exit()


if __name__ == '__main__':
    fn_main()
