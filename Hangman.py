from COLLECTION_OF_WORDS import word_list
import random


random_word=random.choice(word_list)
print("Welcome to Hangman!")
print("Find the word to save the man from hanging!")
print("Shall we start!")
guessed_word=[]
guess_left = 6
while guess_left<100:
    guess=input("Enter the letter that you guessed:")
    if random_word.__contains__(guess):
        print("WOW you guessed a letter in the word!")
        guessed_word.append(guess)
        if guessed_word.__len__()== random_word.__len__():
            print("Congratulations you have saved the man!!!")
            break
        else:
            remaining_letters=random_word.__len__() - guessed_word.__len__()
            print("you have",remaining_letters,"more letters to find the word")
    else:
        guess_left-=1
        print("oops the guessed letter is not in the word!")
        if guess_left==0:
            print("Sorry you can't save the man!!!")
            print("The word was : ",random_word)
            break
        else:
            print("You have only",guess_left,"more guess left!, TRY AGAIN!")
    
