import random

objects = ['rock', 'paper', 'scissors']
choice = ''

run = True
while run == True:
    choice = input("Type 'rock', 'paper', or 'scissors': ")

    gesture = random.choice(objects)
    
    if choice == gesture:
        print('You won')

    else:
        print('You lost')      