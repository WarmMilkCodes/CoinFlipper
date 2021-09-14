import random

coin = ['Heads','Tails']

print('Coin Flipper')

while True:
    flip = input('\nPress enter to flip coin.')
    if flip == '':
        print("\nThe coin landed on " + random.choice(coin))
