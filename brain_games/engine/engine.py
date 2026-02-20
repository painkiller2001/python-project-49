from brain_games.cli import welcome_user

MAX_POINTS = 3


def run_game(game_module):

    user_name = welcome_user()
    
    print(game_module.INTRO)

    points = 0
    while points < MAX_POINTS:
        question, correct_answer = game_module.game()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        
        if str(user_answer).lower() == str(correct_answer).lower():
            print('Correct!')
            points += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return
    
    print(f'Congratulations, {user_name}!')