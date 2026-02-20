from random import randint

INTRO = 'Answer "yes" if the number is even, otherwise answer "no".'


def game():
    
    number = randint(1, 100)

    if number % 2 == 0:
        return number, 'yes'
    else:
        return number, 'no'



