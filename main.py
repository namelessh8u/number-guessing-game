import random


def is_valid(number):
    if number.isdigit():
        return 1 <= int(number) <= max_random
    return False


def enter_number():
    while True:
        user_text = input(f'Enter a real number in the range from 1 to {max_random}.\n')
        if is_valid(user_text):
            user_number = int(user_text)
            global number_of_attempts
            number_of_attempts += 1
            return user_number
        else:
            continue


def compare_numbers(guess):
    while guess != guessing_number:
        if guess < guessing_number:
            print('Your number is less than the correct number. Try once more.')
            guess = enter_number()
        else:
            print('Your number is higher than the correct number. Try once more.')
            guess = enter_number()


def choose_the_difficulty():
    difficulty = 'None'
    while not (difficulty.isdigit()) or difficulty == '0':
        print(
            '''
        Select difficulty:
        Easy - 1
        Medium - 2
        Hard - 3
        1/2/3?
        ''')
        difficulty = input()
    if int(difficulty) > 3:
        print('Congrats! You found a secret difficulty:)')
    random_number = random.randint(1, int(difficulty) * 50)
    return random_number, int(difficulty) * 50


print('\nWelcome to the Number Guessing Game!')
while True:
    number_of_attempts = 0
    guessing_number, max_random = choose_the_difficulty()
    user_guess = enter_number()
    compare_numbers(user_guess)
    print('You guessed it, congratulations!',
          f'Number of attempts: {number_of_attempts}.',
          'Do you want to play again?',
          'y/n?',
          sep='\n')
    if input().lower() != 'y':
        break
print('Thank you for playing the Number Guessing Game. Bye!')
