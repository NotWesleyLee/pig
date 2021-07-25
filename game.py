"""Program that contains all game fuctionality"""

import time
from dice_roll import roll
GOAL = 100

def action(lst, i):
    """Program to roll die and tally points"""
    temp = 0
    num_roll = 0
    checker = False
    print("It's {}'s turn".format(lst[i].name))

    while checker is not True:
        #Players roll dice
        input('Press return to roll the die')
        num_roll += 1
        roll_result = roll(seed=None)
        temp += roll_result

        #Failure
        if roll_result == 1:
            temp = 0
            lst[i].failure()
            time.sleep(1)
            break

        #Display score
        print('You rolled a {}'.format(roll_result))
        time.sleep(1)
        print('\nYou currently have {} temporary points with a total score of {}'
              .format(temp, lst[i].total))
        print('and rolled {} times\n'.format(num_roll))
        time.sleep(1)

        #Determine if player already won
        if lst[i].total + temp >= GOAL:
            break

        #Player chooses to continue rolling or not
        while True:
            keep_rolling = input('Would you like to keep going? (y/n) ')
            if keep_rolling == 'n':
                checker = True
                break
            if keep_rolling != 'y':
                print("Sorry, I didn't quite catch that\n")
                continue
            break
    return temp

def turn_system(lst, i):
    """turn system for multiplayer games"""
    while True:
        time.sleep(1)
        #Call action function
        if lst[i].is_bot is not True:
            temp = action(lst, i)
            lst[i].total += temp
            lst[i].display_stats()
        else:
            #Bot function to play
            temp = action_bot(lst, i)
            lst[i].total += temp
            lst[i].display_stats()

        #Determine if player won
        if lst[i].total >= GOAL:
            break

        #Switch to next player
        if i == len(lst) - 1:
            i = 0
        else:
            i += 1
    return i

def action_bot(lst, i):
    """Function that controls the bot"""
    #Bot's turn
    print("It's {} the bot's turn!".format(lst[i].name))
    time.sleep(1)
    temp = 0
    num_roll = 0
    while True:

        #Determine bot's behavior based on player vs bot score
        if i == 1:
            if lst[0].total > lst[1].total:
                behavior = 15
            else:
                behavior = 8
        else:
            if lst[0].total < lst[1].total:
                behavior = 15
            else:
                behavior = 8

        #Bot rolls
        roll_result = roll(seed=None)
        num_roll += 1
        print('\n{} currently has {} temporary points with a total score of {}'
              .format(lst[i].name, temp, lst[i].total))
        print('and has rolled {} times\n'.format(num_roll))
        print('{} rolled a {}'.format(lst[i].name, roll_result))

        time.sleep(1)

        #Failure state
        if roll_result == 1:
            temp = 0
            lst[i].failure()
            break

        #Determine if bot won
        temp += roll_result
        if lst[i].total + temp >= GOAL:
            break

        #Determine if bot will continue to roll or not
        if temp >= behavior:
            break
    return temp

def turn_order(lst):
    """Function to determine the order of who goes first"""
    i = 0
    for i in range(len(lst)):
        if lst[i].is_bot is False:
            #Roll to for player turn
            input('{}, roll to see who goes first'.format(lst[i].name))
            lst[i].turn = roll(seed=None)
            print('{} rolled a {}\n'.format(lst[i].name, lst[i].turn))
            time.sleep(1)
        else:
            #Bot rolls for turn
            print('{} is going to roll for his turn'.format(lst[i].name))
            lst[i].turn = roll(seed=None)
            print('{} rolled a {}\n'.format(lst[1].name, lst[i].turn))
            time.sleep(1)
    #Reorganize players in correct turn order from highest roll to lowest
    lst.sort(key=lambda x: x.turn, reverse=True)
    print("Here's the turn order:")
    for i in range(len(lst)):
        print("{}: {}".format(i+1, lst[i].name))
    print("")
    time.sleep(1)
    return lst












        #l
