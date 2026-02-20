from random import randint

INTRO = 'What number is missing in the progression?'


def game():

    progression = []
    start = randint(0, 100)
    index = randint(5, 10)
    step = randint(2, 10)
    currentElement = start + index * step
    for i in range(start, currentElement, step):
        progression.append(i)
    
    random_element = progression[randint(0, len(progression)) + 1]
    progression[progression.index(random_element)] = '..'    
    
    return ' '.join(str(i) for i in progression), random_element