# Cipher Program

This program allows users to encrypt or decrypt a string using one of four ciphers: shift cipher, Vigenere cipher, substitution cipher, or transposition cipher.

## Usage

To use the cipher program, run the `cipher.py` script with the following arguments:

```
python cipher.py [cipher] [mode] [key] [text]
```

The `cipher` argument should be one of the following options:

- `shift`: Use the shift cipher.
- `vigenere`: Use the Vigenere cipher.
- `substitution`: Use the substitution cipher.
- `transposition`: Use the transposition cipher.

The `mode` argument should be one of the following options:

- `encrypt`: Encrypt the input text.
- `decrypt`: Decrypt the input text.

The `key` argument is a string that represents the key for the cipher.

The `text` argument is the plaintext or ciphertext to be encrypted or decrypted.

## Examples

To encrypt the plaintext "hello" using a shift cipher with a key of 3, run the following command:
```
python cipher.py shift encrypt 3 hello
```

This will output the encrypted ciphertext: "khoor".

Similarly, to decrypt the ciphertext "khoor" using the same shift cipher and key, run the following command:

```
python cipher.py shift decrypt 3 khoor
```

This will output the decrypted plaintext: "hello".

