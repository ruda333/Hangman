#Hangman Game

import random
from time import sleep

HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  |-+-
 |
 |
 |
 |
 |
 ----------
""",
"""
 ------
 |    |
 |    O
 |  |-+-|
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  |-+-|
 |    |
 |    |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  |-+-|
 |    |
 |    |
 |   | 
 |  | 
 |
 ----------
""",
"""
 ------
 |    |
 |    O
 |  |-+-|
 |    |
 |    |
 |   | |
 |  |   |
 |
 ----------
""")

word=input(str('User1, Enter the word to be guessed:')).upper()
POSITIVE_SAYINGS = ("Well done!", "Awesome!", "You are a Legend!","Wow you are really good at this!","Nice guess!")
MAX_WRONG = 7
so_far = ("-") * len(word)
used = []
wrong = 0

j=0
while(j<50):
    print("********************************************************************************")
    j+=1

print("\t \t \t Welcome to Hangman!")
print("Good luck User2!")
print()
input("Press Enter to START: ")

while (wrong < MAX_WRONG and so_far != word):
    print()
    print(HANGMAN[wrong])
    print("Word so far: ", so_far)
    print("Letters used: ", used)
    print()
    print()
    
    guess = input("Guess a letter: ").upper()

    while(guess in used or len(guess)>1):
        if guess in used:
            print("Try again... You've already used this letter")
            print()
            print()
            guess = input("Guess a letter: ").upper()
        elif(len(guess)>1):
            print("You can input only one letter at a time")
            print()
            print()
            guess = input("Guess a letter: ").upper()
          
    used.append(guess)

    if guess in word:
        print(random.choice(POSITIVE_SAYINGS),"...Updating word so far...")
        print()
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess

            else:
                new += so_far[i]
        so_far = new

    else:
        print("INCORRECT! Try again!")
        print()
        wrong += 1

print("Calculating result...")
if wrong == MAX_WRONG:
    print('''UNLUCKY! You lost     **           **     Better luck next time!)
                     *  *         *  *
                      **           **
                       '     *      '
                       '    * *     '

                          *  *  *
                          *  *  *
                          *  *  *''')
    print(HANGMAN[7])
else:
    print('''WINNER!    **        **    Congratulations!
          *  *      *  *

          *             *
           *           *
             *********''')
    print('''         
                   |  O  /
                    |-+-/
                      |
                      |
                     / |
                    /   |''')
print()
print()
input("Press Enter to Leave: ")

