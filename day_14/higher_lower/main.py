import random
import os
from game_data import data
from art import logo, vs


def format_data(account):
    """Format the account data and return the printable format."""
    return f"{account['name']}, a {account['description']}, from {account['country']}."


def check_answer(choice, a_followers, b_followers):
    """Take a user's guess and followers count and check if they got it right."""
    return (choice == "a" and a_followers > b_followers) or (choice == "b" and b_followers > a_followers)


def update_screen():
    """Clear the user screen and print the game logo."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)


account_a = random.choice(data)

score = 0
game_is_on = True

print(logo)

while game_is_on:

    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    while guess not in ["a", "b"]:
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    update_screen()

    account_a_followers = account_a['follower_count']
    account_b_followers = account_b['follower_count']

    if check_answer(guess, account_a_followers, account_b_followers):
        score += 1
        print(f"You're right! Current score: {score}.\n")
        account_a = account_b
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_is_on = False
