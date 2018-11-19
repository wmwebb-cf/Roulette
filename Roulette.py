"""
WELCOME TO THE BIG HANK'S HOTEL AND CASINO!

Tasks:
[x] Set up the table with proper numbers and colors
[x] Set up ball play that selects a number and a color
[] Declare player(s)
[] Establish initial purse amount and calculate earnings/losses
[] Establis betting scheme
[] Place your bets
[] Play the ball
[x] Determine where the ball landed and display it to the players
[] Calculate payout
[] Play again OR End Game

"""
from beautifultable import BeautifulTable
import random
#dice_one = random.randint(0, 36)


'''
*
Setup table spaces
*
'''

zero_spot = {
    'zero': [0, 0]
    }
red_spot = {
    'red': [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    }
black_spot = {
    'black': [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    }

'''
*
Declare Player
Establish initial purse amount and calculate earnings/losses
*
'''

player_one = input('Player 1, please enter your name: ').capitalize()
player_one_purse = 500


'''
*
Establish betting scheme
*
'''

table = BeautifulTable()
table.column_headers = ['Type of Bet', 'Payout', 'Chance of Winning']
table.append_row(['Reds / Blacks (color)', '1:1', '48.65%'])
table.append_row(['Evens / Odds', '1:1', '48.65%'])
table.append_row(['Lows / Highs (1-18 / 19-36)', '1:1', '48.65%'])
table.append_row(['Dozens', '2:1', '32.43%'])
table.append_row(['Columns', '2:1', '32.43%'])
table.append_row(['6 Numbers (6 line)',	'5:1', '16.22%'])
table.append_row(['4 Numbers (square)',	'8:1',	'10.81%'])
table.append_row(['3 Numbers (street)',	'11:1',	'8.11%'])
table.append_row(['2 Numbers (split)',	'17:1',	'5.41%'])
table.append_row(['1 Number (straight)', '35:1', '2.70%'])
print(table)

'''
*
Place your bets
*
'''

player_bet = int(input(f'{player_one} how much would you like to bet?'))
bet_type = input('What type of bet would you like to make? ')

'''
*
Play the ball: selects a random number from the table

Determine what spot the ball landed on and display it to the players
*
'''

def play_ball():

    ball = random.choice(zero_spot['zero'] + red_spot['red'] + black_spot['black'])
    
    if ball in [x for y in zero_spot.values() for x in y]:
        print(f'ball lands on GREEN: {ball}')
    elif ball in [x for y in red_spot.values() for x in y]:
        print(f'ball lands on RED: {ball}')
    elif ball in [x for y in black_spot.values() for x in y]:
        print(f'ball lands on BLACK: {ball}')


'''
*
Calculate payout
*
'''

'''
*
Play again OR End Game
*
'''


