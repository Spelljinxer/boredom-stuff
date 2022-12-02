
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

    output_word = ""

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
        
        for i in range(len(secretword)):
            self.output_word += "_"
    
    def execute(self):
        if(self.difficulty == 1 or self.difficulty == 2):
                print("Length of the word is: " + str(len(secretword)))
        while(self.round_count < self.guess_count):
            # print("You have " + str(self.guess_count - self.round_count) + " guesses left.")
            guess = input("Enter your guess: ")
            #ask for another input if the guess is longer or shorter than the secret word
            if(len(guess) != len(secretword)):
                print("Your guess is not the same length as the secret word.")
                continue
               

            #place a '*' in the output_word where the guess is correct but in the wrong position,
            #and the letter of the guess where the guess is correct and in the correct position
            for i in range(len(secretword)):
                if(guess[i] == secretword[i]):
                    self.output_word = self.output_word[:i] + guess[i] + self.output_word[i+1:]
                elif(guess[i] in secretword):
                    self.output_word = self.output_word[:i] + "*" + self.output_word[i+1:]

            print("Output : ", self.output_word)
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
    # print("SECRET WORD IS: " + secretword)
    Game.execute()


    
    


