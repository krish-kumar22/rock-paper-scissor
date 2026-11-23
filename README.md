# Rock Paper Scissors

A simple **Rock Paper Scissors** game built in **Python 3**. Play 3-round matches against the computer and keep track of your score.

## Concepts Used

- Conditions (`if` / `elif` / `else`)
- Functions
- Random module (or fixed choices for testing)

## How It Works

- Each match consists of **3 rounds**.
- You enter your choice each round (`rock`, `paper`, or `scissors`).
- The computer picks its choice (random or fixed, depending on mode).
- The winner of each round is determined, and scores are tallied.
- After 3 rounds, the match result is declared.
- You can choose to play another match or exit.

## Setup

1. Make sure you have **Python 3** installed.
2. Clone or download the repository.
3. Run the game:

```bash
python rock_paper_scissors.py
```

## Test Mode

The script includes a **TEST_MODE** flag that uses a fixed sequence of computer choices (`scissors`, `rock`, `paper`) instead of random ones. This is useful for matching known test cases.

- Set `TEST_MODE = True` for deterministic, testable output.
- Set `TEST_MODE = False` for a real random game.

## Functions

| Function | Description |
|---|---|
| `get_winner(player, computer)` | Compares two choices and returns `'player'`, `'computer'`, or `'draw'`. |
| `get_player_choice()` | Prompts the player until a valid choice is entered. |
| `get_computer_choice(round_no)` | Returns the computer's choice (fixed or random). |
| `play_match()` | Plays 3 rounds, tracks scores, and declares the match result. |
| `main()` | Entry point — loops matches until the player quits. |

## Example Output

```
Round 1
Enter rock, paper or scissors: rock
Computer chose: scissors
You win

Round 2
Enter rock, paper or scissors: paper
Computer chose: rock
You win

Round 3
Enter rock, paper or scissors: scissors
Computer chose: paper
You win

Round 1: You win | Round 2: You win | Round 3: You win
You 3 | Computer 0 | Draws 0
Result: You win the match!

Play again? (y/n): n
Thanks for playing!
```

## Author

**krish-kumar22**
