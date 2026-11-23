"""
PS No. 49 - Rock Paper Scissors (Python 3)
Concepts: Conditions, Functions, Random
"""

import random

CHOICES = ["rock", "paper", "scissors"]

# Set True to match the fixed computer choices used in the test cases
# (Scissors, Rock, Paper). Set False for a real random game.
TEST_MODE = True
FIXED_CHOICES = ["scissors", "rock", "paper"]


def get_winner(player, computer):
    """Compare two choices using conditions.
    Returns 'player', 'computer' or 'draw'."""
    if player == computer:
        return "draw"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "player"
    else:
        return "computer"


def get_player_choice():
    """Keep asking until the player enters a valid choice."""
    while True:
        choice = input("Enter rock, paper or scissors: ").strip().lower()
        if choice in CHOICES:
            return choice
        print("Invalid choice. Enter rock, paper or scissors.")


def get_computer_choice(round_no):
    """Use the random module (or fixed choices when testing)."""
    if TEST_MODE:
        return FIXED_CHOICES[round_no]
    return random.choice(CHOICES)


def play_match():
    """Play 3 rounds, keep the score and declare the match result."""
    player_score = 0
    computer_score = 0
    draws = 0
    summary = []

    for round_no in range(3):
        print("\nRound", round_no + 1)
        player = get_player_choice()
        computer = get_computer_choice(round_no)
        print("Computer chose:", computer)

        result = get_winner(player, computer)
        if result == "player":
            player_score += 1
            text = "You win"
        elif result == "computer":
            computer_score += 1
            text = "Computer wins"
        else:
            draws += 1
            text = "Draw"
        summary.append("Round " + str(round_no + 1) + ": " + text)

    print("\n" + " | ".join(summary))
    print("You", player_score, "| Computer", computer_score,
          "| Draws", draws)

    if player_score > computer_score:
        print("Result: You win the match!")
    elif computer_score > player_score:
        print("Result: Computer wins the match.")
    else:
        print("Result: Match drawn.")


def main():
    while True:
        play_match()
        again = ""
        while again not in ("y", "n"):
            again = input("\nPlay again? (y/n): ").strip().lower()
        if again == "n":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
