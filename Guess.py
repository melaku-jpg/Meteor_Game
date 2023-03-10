'''
Requirements for the number guessing game
1. Change the number range from 1 to 1,000,000
2. The game should ask us to give a number
3. Give a glue of the number is higher or lower than the guess
4. Inform the player if he/she won
'''
from random import randint
start = 1
end = 100

value = randint(start,end)

print ("The computer chose a number between", start, "and", end)

guess = None

while guess != value:
    text = input("Guess the number: ")
    guess = int(text)
    if guess < value:
        print ("The number is higher.")
    elif guess > value:
        print ("The number is lower.")
print("Congratulations!! You've guessed the number. You Won")