import random

someWords= ["apple","banana", "mango", "strawberry", "orange", "grape", "pineapple", "apricot", "lemon", "coconut", "watermelon", "cherry", "papaya", "berry", "peach", "lychee", "muskmelon"]
word=random.choice(someWords)
print("Guess the word! HINT: word is a name of a fruit")
print("valid fruits are: apple, banana, mango, strawberry, orange, grape, pineapple, apricot, lemon, coconut, watermelon, cherry, papaya, berry, peach, lychee, muskmelon")
print(len(word),end=' ')
print("letters")
print('-'*len(word))


letterGuessed=''
choice=len(word)+2
try:
    while(choice!=0):
        print()
        choice-=1
        
        guess=input("Enter a letter to guess: ")

        if not guess.isalpha():
            print("letters only")
            continue
        elif len(guess)>1:
            print("single letter only")
            continue
        elif guess in letterGuessed:
            continue
        elif guess in word:
            letterGuessed+=guess

        for i in word:
            if i in letterGuessed:
                print(i,end=' ')
            else:
                print('-',end=' ')

        if len(letterGuessed)==len(word):
            print()
            print("Won!")
            break

    if choice==0:
        print()
        print("Try Again!")
        print("The word was {}".format(word))

except KeyboardInterrupt:
    print()
    print("Bye! Try again!")
    exit()
