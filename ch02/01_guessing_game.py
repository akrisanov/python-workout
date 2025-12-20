import random
import logging

logger = logging.getLogger(__name__)


def guessing_game():
    answer = random.randint(1, 100)
    guesses = 0

    logger.debug(f"The target number is {answer}")

    while guesses < 3:
        try:
            guess_str = input("Guess a number: ").strip()
            guess = int(guess_str)
        except ValueError:
            print("Please enter a valid integer")
            continue
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            return

        guesses += 1

        if guess == answer:
            print("Just right")
            break

        if guess > answer:
            print("Too high")
        elif guess < answer:
            print("Too low")
    else:
        print("You didn't guess in time")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    guessing_game()
