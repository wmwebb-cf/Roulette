"""
WELCOME TO THE BIG HANK'S HOTEL AND CASINO!

Tasks:
[x] Set up the table with proper numbers and colors
[x] Set up ball play that selects a number and a color
[] Declare player(s)
[] Establish initial purse amount and calculate earnings/losses
[x] Establish betting scheme
[] Place your bets
[] Play the ball
[x] Determine where the ball landed and display it to the players
[] Calculate payout
[] Play again OR End Game

"""
from beautifultable import BeautifulTable
import random
#dice_one = random.randint(0, 36)

'''==============================>>
Welcome message
Intro message
Establish Player
Establish initial purse amount and calculate earnings/losses
'''
player_one = ""
player_purse = 0
player_bet_type = 'What type of bet would you like to place? '
player_bet_amount = 'How much would you like to bet? '
player_bet_numbers = []
welcome_message = (
f"""
WELCOME TO THE BIG HANK'S HOTEL AND CASINO

Where you can strike it RICH at the Roulette table!
"""
)

intro_message = (
f"""
~ Here are $500 in chips to start the game.

~ Take a look at our playing table and our betting scheme.

~ Think about where you would like to place you bets.
"""
)


'''==============================>>
Setup table spaces
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

def roulette():
    roulette_table = BeautifulTable()
    roulette_table.insert_column(0, ' ', ['1-Red', '4-Black', '7-Red', '10-Black',
                                        '13-Black', '16-Red', '19-Red', '22-Black',
                                        '25-Red', '28-Black', '31-Black', '34-Red'])
    roulette_table.insert_column(1, '0-Green', ['2-Black', '5-Red', '8-Black', '11-Black',
                                        '14-Red', '17-Black', '20-Black', '23-Red',
                                        '26-Black', '29-Black', '32-Red', '35-Black'])
    roulette_table.insert_column(2, ' ', ['3-Red', '6-Black', '9-Red', '12-Red',
                                        '15-Black', '18-Red', '21-Red', '24-Black',
                                        '27-Red', '30-Red', '33-Black', '36-Red'])
    print(roulette_table)




'''==============================>>
Establish betting scheme
'''

def bet_scheme():
    bet_table = BeautifulTable()
    bet_table.column_headers = ['Type of Bet', 'Payout', 'Chance of Winning']
    bet_table.append_row(['Reds / Blacks (color)', '1:1', '48.65%'])
    bet_table.append_row(['Evens / Odds', '1:1', '48.65%'])
    bet_table.append_row(['Lows / Highs (1-18 / 19-36)', '1:1', '48.65%'])
    bet_table.append_row(['Dozens', '2:1', '32.43%'])
    bet_table.append_row(['Columns', '2:1', '32.43%'])
    bet_table.append_row(['6 Numbers (6 line)',	'5:1', '16.22%'])
    bet_table.append_row(['4 Numbers (square)',	'8:1',	'10.81%'])
    bet_table.append_row(['3 Numbers (street)',	'11:1',	'8.11%'])
    bet_table.append_row(['2 Numbers (split)',	'17:1',	'5.41%'])
    bet_table.append_row(['1 Number (straight)', '35:1', '2.70%'])
    bet_table.column_alignments['Type of Bet'] = BeautifulTable.ALIGN_LEFT
    print(bet_table)

'''==============================>>
Place your bets
'''

def player_num(selected):
  for _ in range(selected):
      value = int(input("Enter the number you are betting on: "))
      player_bet_numbers.append(value)
  print(player_bet_numbers)
  return player_bet_numbers


'''==============================>>
Play the ball: selects a random number from the table
Determine what spot the ball landed on and display it to the players
'''

def play_ball():

    ball = random.choice(zero_spot['zero'] + red_spot['red'] + black_spot['black'])
    
    if ball in [x for y in zero_spot.values() for x in y]:
        return f'ball lands on GREEN: {ball}'
    elif ball in [x for y in red_spot.values() for x in y]:
        return f'ball lands on RED: {ball}'
    elif ball in [x for y in black_spot.values() for x in y]:
        return f'ball lands on BLACK: {ball}'


'''==============================>>
Calculate payout
'''

def payout(amount, bet_type):
    player_purse = player_purse + (amount * bet)
    print(player_purse)
    return player_purse

    reds = black = evens = odds = lows = highs = amount * 1
    dozens = columns = amount * 2
    6line = amount * 5
    square = amount * 8
    street = amount * 11
    split = amount * 17
    straight = amount * 35
    

'''==============================>>
Play again OR End Game
'''





roulette()
bet_scheme()

#bet_type = input('What type of bet would you like to make? ')
#player_bet = int(input(f'{player_one} how much would you like to bet? '))

