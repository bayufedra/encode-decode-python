# encode-decode-python
tools to encoding and decoding strings or cipher, may be can help in CTF

Simple tools for encoding and decoding strings, may be can little help in CTF

there are 2 variant in tools, list mode and argument mode
for list mode, you can running this tools with simple mode, only typing `python file_name.pyc` and you will know how to use it

for argument mode typing `python file_name.pyc -h` for more information
example :

```python
python file_name.pyc -b64 - strings #base64 encode
python file_name.pyc -hex -d hexadecimal_strings #hexadecimal decode
python file_name.pyc -rev strings #reverse strings
python file_name.pyc -rot13 strings #rot13 shift
python file_name.pyc -caes -brute strings #caessar bruteforce for 0-26 shift
python file_name.pyc -caes strings -key (0-26) #caessar shift key value
python file_name.pyc -xor -brute strings #xor bruteforce 00-FF
python file_name.pyc -xor strings -key strings #xoring with key (only print printable char for results)
python file_name.pyc -md5 strings #hashing MD5
```
