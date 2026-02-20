from random import randint

INTRO = 'Find the greatest common divisor of given numbers.'


def game():

    x, y = randint(1, 10), randint(1, 10)

    if x > y:
        while x % y != 0:
            x, y = y, x % y
        return f'{x} {y}', y
    else:
        while y % x != 0:
            x, y = y, x % y
        return f'{x} {y}', x





