from data import data, data_size
from copy import deepcopy
import random


def print_intro():
    print("Welcome to Higher Lower Game!")


def print_options(celeb_dict):
    for key, value in celeb_dict.items():
        print(
            f"{key}: {value['name']}, a {value['description']} from {value['country']}")
        if key == "A":
            print("X")


def choose_celeb(data_):
    celeb = data_.pop(random.choice(range(len(data_))))
    return celeb


def ask_player(celeb):
    AorB = input("Who has more followers? Type 'A' or 'B': ")

    if AorB == "A":
        other = "B"
    else:
        other = "A"

    if celeb[AorB]['follower_count'] > celeb[other]['follower_count']:
        print("You are right! Let's go again.")
        print()
        return celeb[AorB]
    else:
        print("Sorry. You are wrong. You lose!")
        return False


def game():
    data_ = deepcopy(data)
    celeb = {}
    celeb["A"] = choose_celeb(data_)
    points = 0
    print_intro()
    while celeb["A"] and (points < data_size):
        celeb["B"] = choose_celeb(data_)

        print(f"Points: {points}")
        print_options(celeb)

        celeb["A"] = ask_player(celeb)
        points += bool(celeb["A"])

    if points == data_size:
        print("Congratulations! You got everything right! Thanks for playing!")


if __name__ == "__main__":
    game()
