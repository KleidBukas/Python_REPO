import random

SecretNumber = random.randint(1, 100)
print('Guess the number between 1 and 100')

#Ask for a guess
for guesses in range(1,20):
    print('Keep trying.')
    guess = int(input())

    if guess < SecretNumber:
        print('No. Try higher.')
    elif guess > SecretNumber:
        print('No. Try lower.')
    else:
        break

if guess == SecretNumber:
    print('Noice.')