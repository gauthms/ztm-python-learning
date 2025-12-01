import sys
import random


first = int(sys.argv[1])
last = int(sys.argv[2])
random_number = random.randint(first, last)

print(random_number)

while True:
    try:
        number = input('Guess the number!\n')
        if (int(number) == random_number):
            break
        else:
            print('Try again')

    except ValueError:
        print('Please enter a number and try again')
print('You guessed right!')


