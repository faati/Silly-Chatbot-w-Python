
import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
#for multi os support

cls()

print("\n\n\n##### WELCOME TO SILLY CHATBOT #####\n")
name=input("What is your name? ")

cls()

print("\nHello " + name + ", my name is Silly, nice to meet you!")

cls()

how=input("\nHow are you? ")

cls()

age=int(input("\nOh! How old are you? "))

cls()

if age >= 0 and age < 18 :
    print("\nWouv! You are too young! I'm jealous in you. ")
elif age < 30:
    print("\nYou must be making big decisions in these ages!")
elif age < 50:
    print("\nYou must be getting bored with life!")
else:
    print("\nYou are too old man!")

askYN1=input("\n\nWould you like to learn my age? (y/n)")

cls()

if askYN1=="y" :
    print("\nI think you are a little curious. :) No worries, I'm just younger than you. ;)")
elif askYN1=="n":
    print("\nAre you afraid that I'm younger than you? Yes, i'm younger than you! ;)")
else:
    print("\nYou had to press only y or n letter, but no worries, just know that I'm younger than you! ;)")

print('\n\nYou told "' + how + '" when I asked how you are, I think it is related with your horoscope...')

#guessing horoscope game
def horoscope():
    check=0
    print('\nI will guess your horoscope and you just press "y" for yes, and "n" for No.')
    horoscopes=["Gemini", "Virgo", "Scorpio", "Sagittarius", "Aries"]
    askYN3=input("\nLet me guess! Your horoscope is Leo? (y/n) ")
    cls()
    if askYN3=="y":
        print("\nHahaha! I am the master! May be I can tell my secret later... ;)")
        check=1
    else:
        for i, h in enumerate(horoscopes):
            askYN4=input("\nInteresting... Let me guess again: " + h + " (y/n) ")
            if askYN4=="y":
                print("\nBingo!")
                check=1
                break
    
    if check != 1:
        cls()
        print("\nOk, I give up...") 
#end of horoscope game

#finding number 1 to 100 game
def onetoten():
    print('\nChoose a number 1 to 100 and I will try to find it.')
    print('\nEnter "yes" if it is correct\nEnter "down" if your number lower then my guess\nEnter "up" if your number higher than my guess')
    askYN5=input('\nAre you ready? (y/n) ')
    cls()
    if askYN5=="y":
        down=int(1)
        up=int(100)
        askYN6="no"
        while askYN6!="yes":
            guess=int(random.randrange(down, up))
            print('Ok! Here is my guess: ' + str(guess))
            askYN6=input('Is it correct? (yes/up/down)')
            if askYN6=="up":
                down=guess
            elif askYN6=="down":
                up=guess
            elif askYN6=="yes":
                print('\nBingo!')
            else:
                print('\nPlease enter "yes" if it is correct,\n enter "down" if your number lower then my guess,\n enter "up" if your number higher than my guess.')         
    else:
        cls()
        print('\nOk, anyways...')
#end of onetoten game

askYN2=input("\nWould you like me to guess your horoscope? (y/n) ")

cls()

if askYN2=="y" :
    print("\nGreat!")
    horoscope()
elif askYN1=="n":
    print("\nDon't be boring! I have another game for you, let's play!")
    onetoten()
else:
    print("\nYou had to press only y or n letter, but no worries, let's play another game.")
    onetoten()


print("\nThank you " + name + "!\nI think it is enough for today, I'm tired. See you later!\n")