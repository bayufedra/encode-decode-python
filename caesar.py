#!/usr/bin/env python

# Caesar Cipher Encryptions

import argparse
from sys import argv
from string import uppercase, lowercase

class Caesar:
	def __init__(self):
		pass

	def shift(self, text, key):
		result = ""
		for x in range(len(text)):
			if text[x].isalpha():
				if text[x].islower():
					result += lowercase[(lowercase.find(text[x]) + key) % 26]
				else:
					result += uppercase[(uppercase.find(text[x]) + key) % 26]
			else:
				result += text[x]

		return result

	def brute(self, text):
		result = []

		for i in range(26):
			results = ""
			for x in range(len(text)):
				if text[x].isalpha():
					if text[x].islower():
						results += lowercase[(lowercase.find(text[x]) + i) % 26]
					else:
						results += uppercase[(uppercase.find(text[x]) + i) % 26]
				else:
					results += text[x]
			
			result.append(results)

		return result


def main():
	arg	= argparse.ArgumentParser(
			description = "[+] Caesar Cipher Encryptions",
			usage = """{0} [-h] [-b] [-k [0-25]] CIPHER\nexample:\n [+] {0} -b SAMPLE\n [+] {0} -k 1 SAMPLE""".format(argv[0])
	)
	
	arg.add_argument("str", help="Plain Text")
	arg.add_argument("-b", "--brute", action="store_true", help="Bruteforce shift key 0-25")
	arg.add_argument("-k", "--key", type=int, action="store", help="Using spesific shift key")

	args	= arg.parse_args()
	ex		= Caesar()

	if args.brute:
		res = ex.brute(args.str)

		for i in range(len(res)):
			print "[+] Key {}, result: {}".format(i, res[i]) 
	elif args.key:
		if args.key <= 25 >= 0:
			print "[+] Result:", ex.shift(args.str, args.key)
		else:
			print "[!] Key must be between 0-25"

if __name__ == '__main__':
	main()