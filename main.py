import numbers
import random

print('NUMBER GUESSING GAME')

r1 = random.randint(1, 9)

chances = 0
while chances < 5:
    guess=int(input('enter a number: '))


    if guess == r1:
        print('congratulations u won the game!!')
        break


    elif guess < r1:
        print('ur guess was too low,guess a no. higher than ',guess)


    else:
        print('ur guess was too high,guess a no. lower than',guess)


    chances+=1

if not chances < 5:
    print('you lost the game!!!')

    







