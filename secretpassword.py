'''
Crack the secret password program
'''

import sys
import string
import itertools

password = 'secret'

def hash(password):
    return ''.join([chr(ord(c) + 1) for c in password])

def crack(hash):
    for i in range(1, 5):
        for guess in itertools.product(string.ascii_lowercase, repeat=i):
            guess = ''.join(guess)
            if hash(guess) == hash:
                return guess

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(crack(hash(sys.argv[1])))
    else:
        print('Usage: python secretpassword.py <password>')
