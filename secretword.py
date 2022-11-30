
import random
import sys
import os
import prettytable

secretword = ""

with open("words.txt") as f:
    secretword = random.choice(f.readlines()).strip()

class Game:
    guess_count = 0
    round_count = 0 
    difficulty = 0

    def __init__(self, difficulty):
        self.difficulty = int(difficulty)
        if(self.difficulty) == 1:
            self.guess_count = 25
        elif(self.difficulty) == 2:
            self.guess_count = 20
        elif(self.difficulty) == 3:
            self.guess_count = 15
        elif(self.difficulty) == 4:
            self.guess_count = 10
        elif(self.difficulty) == 5:
            self.guess_count = 5
        
    def execute(self):
        while(self.round_count < self.guess_count):
            print("You have " + str(self.guess_count - self.round_count) + " guesses left.")
            guess = input("Enter your guess: ")
            if(guess == secretword):
                print("You won in " + str(self.round_count) + " guesses!")
                break
            
            #check position of letters in guess
            table = prettytable.PrettyTable(["Letter", "Position"])
            for i in range(0, len(guess)):
                if(guess[i] == secretword[i]):
                    table.add_row([guess[i], "Correct"])
                else:
                    table.add_row([guess[i], "Wrong"])
            print(table)

            self.round_count += 1
        
        print("You lost! The word was " + secretword + ".")


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
    
    Game = Game(sys.argv[2])
    Game.execute()


    
    


