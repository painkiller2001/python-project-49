from random import randint

INTRO = 'What is the result of the expression?'


def game():
    
    operations_list = {
        1: lambda x, y: x - y,
        2: lambda x, y: x * y,
        3: lambda x, y: x + y
    }
    
    x, y = randint(1, 10), randint(1, 10)
    op_num = randint(1, 3)
    correct_answer = operations_list[op_num](x, y)
    match op_num:
        case 1:
            expression = f'{x} - {y}'
        case 2:
            expression = f'{x} * {y}'
        case 3:
            expression = f'{x} + {y}'
    return expression, correct_answer



