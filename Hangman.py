import random   #used for Random valurs
import time     #used for Time

#initial Steps to invite Player in the Game

print("\n *******************🙇️  WELCOME TO HANGMAN GAME  🙇**************************** ")

name=input("ENTER YOUR NAME : ")
print("HELLO 🙋‍ "+name+"! BEST OF LUCK 👍")

time.sleep(1)   #This is used to halt the execution of the program for a few seconds.

print("THE GAME IS ABOUT TO START!\n LET'S PLAY HANGMAN")

time.sleep(1)


#main() Function
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme\n"
                    "damage","plants","rainbow","computer","science","programming","python","mathematics","player","condition\n" 
                    "reverse","water","board","geeks"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = "_" * length
    already_guessed = []
    play_game = ""

#A Loop to re-execute the game when the first round ends

def play_loop():
    global play_loop
    play_game = input("DO YOU WANNA PLAY AGAIN? Y = YES 👍, N = NO 👎\n")
    while play_game not in ["y","Y","n","N"]:
        play_game = input("DO YOU WANNA PLAY AGAIN? Y = YES 👍, N = NO 👎\n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("THANKS FOR PLAYING! WE EXPECT YOU BACK AGAIN 😊")
        exit()

#Function for the HangMan Activity

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game

    limit = 5
    guess = input("THIS IS THR HANGMAN WORD : "+display+" \n ENTER YOUR GUESS : \n")
    guess = guess.strip()

    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("INVALID INPUT ◑﹏◐ , TRY A LETTER \n")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("TRY ANOTHER LETTER ✍(◔◡◔) \n")


    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print(" +_+      O0PS   \n")
            print("WRONG GUESS.... YOU HAVE "+str(limit - count)+"GUESS REMAINING\n")

        elif count == 2:
            time.sleep(1)
            print("  =_=      O0PS   \n")
            print("WRONG GUESS.... YOU HAVE " + str(limit - count) + "GUESS REMAINING\n")


        elif count == 3:
            time.sleep(1)
            print("   X_X     O0PS   \n")
            print("WRONG GUESS.... YOU HAVE " + str(limit - count) + "GUESS REMAINING\n")


        elif count == 4:
            time.sleep(1)
            print("   ( ﾉ ﾟｰﾟ)ﾉ)    O0PS   \n")
            print("WRONG GUESS.... YOU HAVE " + str(limit - count) + "GUESS REMAINING\n")


        elif count == 5:
            time.sleep(1)
            print("   ◑﹏◐        O0PS   \n")
            print("WRONG GUESS.... YOU HAVE " + str(limit - count) + "GUESS REMAINING\n")

    if word == '_' * length:
        print("CONGRATS! YOU HAVE GUESS THE  WORD CORRECTLY!")
        play_loop()
    elif count != limit:
        hangman()

main()

hangman()