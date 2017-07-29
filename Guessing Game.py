import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 10)
print(number)
print('Well, ' + myName + ', I am thinking of a number between 1 and 10.')

while guessesTaken < 3:
    print('Take a guess.') # There are four spaces in front of print.
    guess = int(input())



    guessesTaken = guessesTaken + 1

    if guess == number:
        print('You Got It!!!!')
        break

    elif guess == (number - 1) or (guess == number + 1):
        print('Your HOT!!') # There are eight spaces in front of print.

    elif guess == (number - 2) or guess == (number + 2):
         print('Your WARM!!')

    else:
        print('Your cold as Hell')

    if guessesTaken == 3:
        print('Out of Turns, Your a Failure')

