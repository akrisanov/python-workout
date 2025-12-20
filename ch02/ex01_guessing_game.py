import random
import logging

logger = logging.getLogger(__name__)


def guessing_game():
    answer = random.randint(1, 100)
    logger.debug(f"The target number is {answer}")

    while True:
        try:
            guess_str = input("Guess a number: ").strip()
            guess = int(guess_str)
        except ValueError:
            print("Please enter a valid integer")
            continue
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            return

        if guess > answer:
            print("Too high")
        elif guess < answer:
            print("Too low")
        else:
            print("Just right")
            break


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    guessing_game()
