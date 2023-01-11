import random
correctGuess = random.randint(1, 20)
print("Guess your number in 10 tries")
for guess in range (1, 10):
    guess = int(input())
    if guess < correctGuess:
        print("Larger number")
    elif guess > correctGuess:
        print("Smaller number")
    else:
        break
if guess==correctGuess:
    print("Correct Number")