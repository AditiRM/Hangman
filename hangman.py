import random
import time
import string
from clue import give_clue

#Opened text file containing 1000 familiar words and stored all the words in file in the list
#'words' is a list of words in python
with open('Mywords.txt') as f:
    words = list(f)


#We will start the game !
print("!!!WELCOME TO HANGMAN !!!")
time.sleep(0.8)
print("Are u ready to start playing?\n")

game_start = input("Press Y for yes or N for no \n")
game_start = game_start.lower()

#Note :strip function is used to remove blank spaces at the start and end of the string
#(used because our words are stored in newline new word format)

while game_start == 'y' :
    word = random.choice(words).strip()
    word_length = len(word)

    print("\nEvery wrong guess of a letter , will decrease your points")
    time.sleep(0.8)
    print("You can only guess wrong 8 times, if don't want to \'leave yourself hanging\'")
    time.sleep(0.8)

    chances = 8
    attempts = 0

    time.sleep(0.8)
    print("\nThe hidden word is {} letters long. Fill in blanks!".format(word_length))

    #Creation of series of astericks that will be switched by the letters the user guessed
    word_guess = ''
    for i in range(word_length):
        word_guess += '*'
    time.sleep(0.8)
    print("\n" + word_guess)

    #For offering clue to the user for guessing the word
    time.sleep(0.8)
    print("Do you want to start with a little clue?")
    with_clue = input("\nPress Y for Yes and N for No \n")
    with_clue = with_clue.lower()

    if with_clue == 'y':
        time.sleep(0.8)
        word_guess = give_clue(word)
        time.sleep(0.8)
        print("\nThere you go buddy: " + word_guess)
        time.sleep(0.8)
        #REMINDER MESSEGE
        print("\nREMEMBER : The hidden word is {} letters long.".format(word_length))

    if with_clue == 'n' :
        time.sleep(0.4)
        print("Alright then go ahead ...")
        time.sleep(0.4)

    while word_guess != word :
        #MAKES A LIST OUT OF THE ASTERICK SERIES , IN ORDER FOR THEM TO BE SWITCHABLE
        word_guess_list = [word_guess[i] for i in range(word_length)]
        #First chance
        if chances == 8 :
            if attempts == 0:
                letter_guess = input("Try your first guess...\n")
                attempts +=1

            elif attempts > 0 :
                time.sleep(0.6)
                #TO KEEP USER'S PROGRESS VISIBLE
                print("Your progress so far :" + word_guess)

                letter_guess = input("Insert a new letter\n")
                attempts += 1

        elif chances < 8 and chances > 1 :
            time.sleep(0.6)
            print("Your progress so far :" + word_guess)
            letter_guess = input("Insert a new letter\n")
            attempts += 1

        #RREMINDER AT LAST ATTEMPT
        elif chances == 1 :
            time.sleep(0.6)

            print("Your progress so far :" + word_guess)
            time.sleep(0.4)
            
            letter_guess = input("\nThis is your last chance buddy!!!\n")
            attempts += 1

        elif chances == 0 or chances < 0 :
            print("You have lost after {} attempts. Well played!".format(attempts))
            time.sleep(0.4)
            print("The word u were looking for is {}\n".format(word))
            break
        
        #CHECKING OF POSSIBLE ERRORS MADE BY USER
        #1) MORE THAN ONE LETTER AS A INPUT
        #2) SYMBOLS OR INPUT OTHER THAN LETTER IS GIVEN BY USER
        time.sleep(0.6)
        letter_guess = letter_guess.lower()
        if len(letter_guess) > 1 :
            print("Dude, that is not fair!\nYou can only guess one letter at a time.")
            time.sleep(0.4)
            print("We will let that slide.Try again Buddy.\n")

        elif letter_guess not in string.ascii_letters:
            print("Symbols are never part of the word")
            time.sleep(0.6)
            print("Try again...\n")

        if letter_guess in word_guess:
            letter_guess = input("You already tried that letter\nOnce is enough! Try again...\n")

        letter_guess = letter_guess.lower()

        #CHEK IF CORRECT OR INCORRECT
        #if incorrect : subtracts a chance left, invites user to prompt new guess
        if letter_guess not in word:
                chances -= 1
                print("\nSorry!! The letter you chose is not contained in the hidden word.")
                time.sleep(0.6)

                print("\nYou have {} chances left now".format(chances))

        #if correct : switches astericks for correct letter, invites user to guess next letter
        if letter_guess in word :
            print("\nGreat!The letter {} is in the hidden word.".format(letter_guess))
            time.sleep(0.6)

            for i in range(len(word_guess_list)) :
                if word[i] ==letter_guess :
                    word_guess_list[i] = letter_guess
            word_guess = ''.join(word_guess_list)

        #User won.
        if word_guess == word :
            time.sleep(0.6)
            print("CONGRATULATIONS!! YOU WON!!!")   
            time.sleep(0.4)

    #INVITATION FOR NEW GAME
    print("Do u want to play again?")
    game_start = input("\nPress Y for yes or N for No\n")
    game_start = game_start.lower()
    if game_start == 'n' :
        time.sleep(0.5)
        print("WELL Played!!!\nGoodbye then:))")
        break




        

        


            


         




