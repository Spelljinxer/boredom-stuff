
import random
import sys
import os
import prettytable

secretword = ""

with open("words.txt") as f:
    secretword = random.choice(f.readlines()).strip()


#----------------- main func ----------------------
def print_usage():
    print("""
        Usage: python secretword.py -d <difficulty>
            -d <difficulty> 1-5 
    """)

if __name__ == '__main__':
    if(len(sys.argv) != 3):
        print_usage()
        sys.exit(1)
    if(sys.argv[1] != "-d"):
        print_usage()
        sys.exit(1)
    if(sys.argv[2] not in ["1", "2", "3", "4", "5"]):
        print_usage()
        sys.exit(1)
    print("You have chosen to play on difficulty level " + sys.argv[2])
    user_guess = input("Guess the secret word: ")
