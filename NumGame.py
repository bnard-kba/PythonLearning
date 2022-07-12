#Number guessing game
import random

print('I am thinking of a number between 1 and 20.')
secretNum = random.randint(1,20)
for i in range(1,6):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNum:
        print('Your guess is too low.')
        continue
    elif guess > secretNum:
        print('Your guess is too high.')
        continue
    else:
        break
if guess == secretNum:
    print('Good job! You guessed my number in ' + str(i) + ' guesses!')
else:
    print('you lose, the number was ' + str(secretNum))


