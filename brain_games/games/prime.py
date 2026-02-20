from math import isqrt
from random import randint

INTRO = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game():

    number = randint(1, 11)
    
    if number <= 1:
        return number, 'no'
    if number == 2:
        return number, 'yes'
    if number % 2 == 0:
        return number, 'no'

    for i in range(3, isqrt(number) + 1, 2):
        if number % i == 0:
            return number, 'no'
    
    return number, 'yes'


