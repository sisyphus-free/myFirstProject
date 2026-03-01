# Beginner Project: Number Guessing Game (Python)

Welcome! We'll learn programming by building a tiny project **step by step**.

## What you'll learn

By the end, you'll understand:

1. Variables
2. Input and output
3. `if` statements
4. Loops
5. Functions
6. Basic debugging

---

## Project goal

Build a terminal game where:

- The computer picks a secret number from 1 to 20.
- The player guesses.
- The game tells the player "too high" or "too low".
- The player wins when they guess correctly.

---

## Step 0: Setup (complete this first)

### 0.1 Check Python is installed

Run:

```bash
python3 --version
```

You should see something like `Python 3.10.x` or newer.

If this command fails, install Python from [python.org](https://www.python.org/downloads/), then run the command again.

### 0.2 Confirm project files exist

In this folder, you should have:

- `README.md`
- `game.py`

### 0.3 Run the game

```bash
python3 game.py
```

Expected first output:

- `Welcome to the Number Guessing Game!`
- `I'm thinking of a number from 1 to 20.`

### 0.4 Step 0 done checklist

Mark this complete when all are true:

- [ ] `python3 --version` works
- [ ] `python3 game.py` starts without crashing
- [ ] You can type a guess and press Enter

---

## Step 1: Print text

Open `game.py` and find:

```python
print("Welcome to the Number Guessing Game!")
```

That line sends text to the terminal.

---

## Step 2: Variables

Find:

```python
secret_number = random.randint(1, MAX_NUMBER)
```

- `secret_number` stores data.
- `random.randint(1, MAX_NUMBER)` picks a random number.

---

## Step 3: User input

Find the `read_guess()` function. It uses:

```python
raw_value = input("Enter your guess: ")
```

- `input(...)` returns text.
- `int(raw_value)` converts text to a number.

---

## Step 4: Conditions (`if` / `elif` / `else`)

Find `compare_guess(...)`:

- If guess is smaller than secret number → return "too low".
- If guess is bigger than secret number → return "too high".
- Otherwise → correct.

---

## Step 5: Loops

Find this loop:

```python
while attempts_left > 0:
```

This repeats until the player runs out of attempts or wins.

---

## Step 6: Functions

Functions break code into small reusable pieces:

- `read_guess(...)`
- `compare_guess(...)`
- `play_game()`

This makes code easier to read and test.

---

## Step 7: Mini challenges (recommended)

Try these in order:

1. Change `MAX_NUMBER` from `20` to `50`.
2. Increase `MAX_ATTEMPTS`.
3. Add a hint: tell whether the secret number is even or odd.
4. Ask the player if they want to play again.

---

## Common beginner mistakes

- Forgetting `:` after `if` or `while`
- Wrong indentation
- Not converting input text to `int`
- Comparing text with numbers

If you see an error, read it slowly. Python's error messages are helpful.

---

## Next project ideas

After this game, we can build:

1. A calculator
2. A to-do list app
3. A quiz game with score tracking

If you want, we'll continue step by step and build one of these together next.
