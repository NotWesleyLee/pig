#!/usr/bin/env python3
""" Pig game written in Python3 """

import time
from player import Player
# from player import AI
from game import turn_system
from game import turn_order


__author__ = 'Wesley Lee'
__email__ = 'shotun123@csu.fullerton.edu'
__maintainer__ = 'shotun123'

def main():
    """The main function of the program"""

    #Initialize list
    k = 0
    lst = []
    print('Hello and Welcome to my Pig game! \n ')

    #Input number of players
    while True:
        player_count = int(input('Start by entering the amount of people will be playing (1-4): '))
        if player_count in range(1, 5):
            break
        print('Sorry that amount of players is unsupported =(')

        #Input play names
    for i in range(player_count):
        lst.append(input('Please enter your name: '))
        print('{} has entered the game!\n'.format(lst[i]))
        lst[i] = Player(lst[i], 0, 0, False)
    if player_count == 1:
        #Add bot
        lst.append("Hugo")
        lst[1] = Player(lst[1], 0, 0, True)
        time.sleep(1)
        print('{} the bot has entered the game!\n'.format(lst[1].name))
        time.sleep(1)
    lst = turn_order(lst)

    #Call function to begin game
    i = turn_system(lst, k)


        #Announce the winner
    time.sleep(1)
    print('\nCongratulations {}! You Win!'.format(lst[i].name))

if __name__ == '__main__':
    main()
