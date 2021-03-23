# encoding=utf-8
#longbotton python guess game
import random

secret_number = random.randint(0, 10)
count = 0
trial = 3

while count < 3:
    guess = int(input('Guess > '))
    count += 1
    if (guess == secret_number):
        print('Correct !')
        print(f'secret number is {secret_number}')
        break

else:
    print('Sorry You failed !)
    print(f'secret number is {secret_number}')