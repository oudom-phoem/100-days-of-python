import random
import os
import art

BLACKJACK = 21
DEALER_MIN_SCORE = 17


def play_blackjack_game():
    """
    Implementation of blackjack game

    Returns:
    user_cards (list): User cards
    computer_cards (list): Computer cards
    user_score (int): User score
    computer_score (int): Computer score
    """
    is_playing_game = True
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = 0
    computer_score = 0

    while is_playing_game:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if computer_score == 0 or user_score == 0 or user_score > BLACKJACK:
            is_playing_game = False
        else:
            user_should_deal = ask_user_for_card()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            elif user_should_deal == 'n':
                computer_cards, computer_score = dealer_turn(computer_cards, computer_score)
                is_playing_game = False

    return user_cards, computer_cards, user_score, computer_score


def deal_card():
    """
    Deal new a new card to a player.

    Returns:
    list: A new card
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """
    Calculate player score

    Parameters:
    cards (list): The player cards

    Returns:
    int: score calculated from the cards
    """
    total_score = sum(cards)
    if total_score == BLACKJACK and len(cards) == 2:
        return 0
    elif 11 in cards and total_score > BLACKJACK:
        for i in range(len(cards)):
            if cards[i] == 11:
                cards[i] = 1
        return sum(cards)   
    return total_score


def ask_user_for_card():
    while True:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if user_should_deal in ['y', 'n']:
            return user_should_deal
        print("Invalid input! Please type 'y' or 'n'.")


def dealer_turn(computer_cards, computer_score):
    while computer_score < DEALER_MIN_SCORE:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    return computer_cards, computer_score


def compare(user_score, computer_score):
    """
    Compare user and computer score.

    Parameters:
    user_score (int): User score
    computer_score (int): Computer score

    Returns:
    string: Text to tell user who win the game
    """
    if computer_score == 0:
        return "Lose, opponent has a blackjack 😱"
    elif user_score == 0:
        return "Win with a blackjack 😎"
    elif user_score > BLACKJACK:
        return "You went over. You lose 😭"
    elif computer_score > BLACKJACK:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    elif computer_score > user_score:
        return "You lose 😤"
    else:
        return "Draw 🙃"


def output_final_cards(user_cards, computer_cards, user_score, computer_score):
    """
    Output final cards and score of user and computer.

    Parameters:
    user_cards (list): User cards
    computer_cards (list): Computer cards
    user_score (int): User score
    computer_score (int): Computer score
    Returns:
    string: Text to show user the final cards and score
    """
    print(f"  Your final hand: {user_cards}, final score {user_score}")
    print(f"  Computer's final hand: {computer_cards}, final score {computer_score}")


def clear_screen():
    """
    Clear screen base on Operating System of the user.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    """
    The main function to start the game by repeating asking user to play game or not.
    """
    while input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower() == "y":
        clear_screen()
        print(art.logo)
        user_cards, computer_cards, user_score, computer_score = play_blackjack_game()
        output_final_cards(user_cards, computer_cards, user_score, computer_score)
        print(compare(user_score, computer_score))
    else:
        print("Goodbye, thank you.")


if __name__ == "__main__":
    main()
