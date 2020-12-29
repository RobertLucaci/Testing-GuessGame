from random import randint


def guess_game(guess, answer):
    if 1 <= guess <= 10:
        if guess == answer:
            print('Congratulation! You guessed the number.')
            return True
        else:
            print('Ehh! Try again!')
            return False
    else:
        print(f'Give a number between 1 and 10.')
        return False


if __name__ == '__main__':
    answer = randint(1, 10)
    while True:
        try:
            guess = int(input(f'Guess a number from 1 to 10: '))
            if guess_game(guess, answer):
                break
            else:
                continue
        except ValueError:
            print('You must enter a number.')
            continue
