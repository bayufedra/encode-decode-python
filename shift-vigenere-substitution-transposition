#!/usr/bin/env python3

import argparse

def shift_encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        if letter.isalpha():
            shifted = (ord(letter) - 65 + key) % 26
            ciphertext += chr(shifted + 65)
        else:
            ciphertext += letter
    return ciphertext

def shift_decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        if letter.isalpha():
            shifted = (ord(letter) - 65 - key) % 26
            plaintext += chr(shifted + 65)
        else:
            plaintext += letter
    return plaintext

def vigenere_encrypt(plaintext, key):
    ciphertext = ''
    key_index = 0
    for letter in plaintext:
        if letter.isalpha():
            shift = ord(key[key_index].upper()) - 65
            shifted = (ord(letter.upper()) - 65 + shift) % 26
            ciphertext += chr(shifted + 65)
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += letter
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    plaintext = ''
    key_index = 0
    for letter in ciphertext:
        if letter.isalpha():
            shift = ord(key[key_index].upper()) - 65
            shifted = (ord(letter.upper()) - 65 - shift) % 26
            plaintext += chr(shifted + 65)
            key_index = (key_index + 1) % len(key)
        else:
            plaintext += letter
    return plaintext

def substitution_encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        if letter.isalpha():
            if letter.islower():
                ciphertext += key[ord(letter) - 97]
            else:
                ciphertext += key[ord(letter) - 65].upper()
        else:
            ciphertext += letter
    return ciphertext

def substitution_decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        if letter.isalpha():
            if letter.islower():
                plaintext += chr(key.index(letter))
            else:
                plaintext += chr(key.index(letter.lower())).upper()
        else:
            plaintext += letter
    return plaintext

def transposition_encrypt(plaintext, key):
    num_columns = len(key)
    num_rows = (len(plaintext) + num_columns - 1) // num_columns
    plaintext += ' ' * (num_rows * num_columns - len(plaintext))
    matrix = [list(plaintext[i:i+num_columns]) for i in range(0, num_rows*num_columns, num_columns)]
    transposed = [''.join(row) for row in zip(*matrix)]
    order = [key.index(str(i+1)) for i in range(num_columns)]
    ciphertext = ''.join([transposed[i] for i in order])
    return ciphertext

def transposition_decrypt(ciphertext, key):
    num_columns = len(key)
    num_rows = (len(ciphertext) + num_columns - 1) // num_columns
    matrix = [list(ciphertext[i:i+num_rows]) for i in range(0, num_columns*num_rows, num_rows)]
    order = [key.index(str(i+1)) for i in range(num_columns)]
    transposed = [''.join(row) for row in zip(*[matrix[i] for i in order])]
    plaintext = ''.join(transposed).rstrip()
    return plaintext

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Encrypt or decrypt a string using a shift cipher, Vigenere cipher, substitution cipher, or transposition cipher')
    parser.add_argument('cipher', type=str, choices=['shift', 'vigenere', 'substitution', 'transposition'], help='the cipher to use')
    parser.add_argument('mode', type=str, choices=['encrypt', 'decrypt'], help='the mode (encrypt or decrypt)')
    parser.add_argument('key', type=str, help='the key to use for the cipher')
    parser.add_argument('text', type=str, help='the plaintext or ciphertext')
    args = parser.parse_args()

    if args.cipher == 'shift':
        if args.mode == 'encrypt':
            ciphertext = shift_encrypt(args.text, int(args.key))
            print(ciphertext)
        else:
            plaintext = shift_decrypt(args.text, int(args.key))
            print(plaintext)
    elif args.cipher == 'vigenere':
        if args.mode == 'encrypt':
            ciphertext = vigenere_encrypt(args.text, args.key)
            print(ciphertext)
        else:
            plaintext = vigenere_decrypt(args.text, args.key)
            print(plaintext)
    elif args.cipher == 'substitution':
        if args.mode == 'encrypt':
            ciphertext = substitution_encrypt(args.text, args.key)
            print(ciphertext)
        else:
            plaintext = substitution_decrypt(args.text, args.key)
            print(plaintext)
    elif args.cipher == 'transposition':
        if args.mode == 'encrypt':
            ciphertext = transposition_encrypt(args.text, args.key)
            print(ciphertext)
        else:
            plaintext = transposition_decrypt(args.text, args.key)
            print(plaintext)
