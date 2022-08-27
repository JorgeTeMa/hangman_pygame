import os
import random
from tkinter import Y


def hangman ():
    word = []
    with open("./data/data.txt", "r", encoding="utf-8") as f:
        ignore = "\n"
        for line in f:
            for x in range (len(ignore)):
                line = line.replace(ignore[x],"")
            word.append(line)
        y = random.choice(word)
        word_chosen = [letter for letter in y]
        word_chosen_underscore = ["__"] * len(word_chosen)
        dictionay_letters = {}
        for ind, letter in enumerate(y):
            if not dictionay_letters.get(letter):
                dictionay_letters[letter] = []
            dictionay_letters[letter].append(ind)
        
        while True:
                print ("""
    $$\   $$\  $$$$$$\  $$\   $$\  $$$$$$\  $$\      $$\  $$$$$$\  $$\   $$\ 
    $$ |  $$ |$$  __$$\ $$$\  $$ |$$  __$$\ $$$\    $$$ |$$  __$$\ $$$\  $$ |
    $$ |  $$ |$$ /  $$ |$$$$\ $$ |$$ /  \__|$$$$\  $$$$ |$$ /  $$ |$$$$\ $$ |
    $$$$$$$$ |$$$$$$$$ |$$ $$\$$ |$$ |$$$$\ $$\$$\$$ $$ |$$$$$$$$ |$$ $$\$$ |
    $$  __$$ |$$  __$$ |$$ \$$$$ |$$ |\_$$ |$$ \$$$  $$ |$$  __$$ |$$ \$$$$ |
    $$ |  $$ |$$ |  $$ |$$ |\$$$ |$$ |  $$ |$$ |\$  /$$ |$$ |  $$ |$$ |\$$$ |
    $$ |  $$ |$$ |  $$ |$$ | \$$ |\$$$$$$  |$$ | \_/ $$ |$$ |  $$ |$$ | \$$ |
    \__|  \__|\__|  \__|\__|  \__| \______/ \__|     \__|\__|  \__|\__|  \__
                            WELCOME TO THE HANGMAN GAME
                            
                            
                            
                            """)
                os.system('clear')
                for element in word_chosen_underscore:
                    print(element + " ", end=" ")
                print("\n")

                letter = input("Ingresa una letra: ").strip().upper()
                assert letter.isalpha(), "Solo letras"

                if letter in word_chosen:
                    for idx in dictionay_letters:
                        word_chosen_underscore[idx] = letter
                
                if "__" not in word_chosen_underscore:
                    os.system('clear')
                    print("Ganador!")
                    break




def run () :

    hangman ()

if __name__ == '__main__' :
    run()