""" Tasks: [x] Set up the table with proper numbers and colors [x] Set
up ball play that selects a number and a color [x] Declare player(s) [x]
Establish initial purse amount and calculate earnings/losses [x]
Establish betting scheme [x] Place your bets [x] Play the ball [x]
Determine where the ball landed and display it to the players [x]
Calculate payout [] Play again OR End Game

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

player_one = ''
player_purse = 500
player_bet_type = 'What type of bet would you like to place?'
player_bet_amount = 'How much would you like to bet?'
player_payout = 0
player_bet_numbers = []
inside_bet = []
player_name = input(f'Hello new player. Please enter your Name: ').capitalize()

welcome_message = (
f"""
{player_name}, WELCOME TO BIG HANK'S HOTEL AND CASINO

Where you can strike it RICH at the Roulette table!
"""
)

intro_message = (
f"""
~ {player_name}, here are $500 in chips to get you started.

~ Take a look at our playing table and our betting scheme above.

~ Think about where you would like to place your bets.
"""
)


'''==============================>>
Setup table spaces
'''
table = [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
         15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
         28, 29, 30, 31, 32, 33, 34, 35, 36]
zero = [0, 0]
reds = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
blacks = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
lows = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
highs = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
columns1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
columns2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
columns3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
dozens1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
dozens2 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
dozens3 = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]


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
    bet_table.append_row(['Dozens 1: 1-12', '2:1', '32.43%'])
    bet_table.append_row(['Dozens 2: 13-24', '2:1', '32.43%'])
    bet_table.append_row(['Dozens 3: 25-36', '2:1', '32.43%'])
    bet_table.append_row(['Columns 1: 1-34', '2:1', '32.43%'])
    bet_table.append_row(['Columns 2: 2-35', '2:1', '32.43%'])
    bet_table.append_row(['Columns 3: 3-36', '2:1', '32.43%'])
    bet_table.append_row(['6 Numbers (6 line)',	'5:1', '16.22%'])
    bet_table.append_row(['4 Numbers (square)',	'8:1',	'10.81%'])
    bet_table.append_row(['3 Numbers (street)',	'11:1',	'8.11%'])
    bet_table.append_row(['Zero Row (split)',	'17:1',	'5.41%'])
    bet_table.append_row(['Split(2 numbers)',	'17:1',	'5.41%'])
    bet_table.append_row(['Straight(1 number)', '35:1', '2.70%'])
    bet_table.column_alignments['Type of Bet'] = BeautifulTable.ALIGN_LEFT
    print(bet_table)

'''==============================>>
Place your bets
'''

def selected_player_num(selected):
  for _ in range(selected):
      value = int(input("{player_name}, enter the number you would like to bet on: "))
      player_bet_numbers.append(value)
  print(player_bet_numbers)
  return player_bet_numbers

def player_numbers(i, n):

    if i == 'reds':
        n.extend(reds)
    elif i == 'blacks':
        n.extend(blacks)
    elif i == 'evens':
        n.extend(evens)
    elif i == 'odds':
        n.extend(odds)
    elif i == 'lows':
        n.extend(lows)
    elif i == 'highs':
        n.extend(highs)
    elif i == 'dozens 1':
        n.extend(dozens1)
    elif i == 'dozens 2':
        n.extend(dozens2)
    elif i == 'dozens 3':
        n.extend(dozens3)
    elif i == 'columns 1':
        n.extend(columns1)
    elif i == 'columns 2':
        n.extend(columns2)
    elif i == 'columns 3':
        n.extend(columns3)
    elif i == 'zero row':
        n.extend(zero)
    elif i == 'six line':
        selected_player_num(6)
    elif i == 'square':
        selected_player_num(4)
    elif i == 'street':
        selected_player_num(3)
    elif i == 'split':
        selected_player_num(2)
    elif i == 'straight':
        selected_player_num(1)

    return n
    


'''==============================>>
Play the ball: selects a random number from the table
Determine what spot the ball landed on and display it to the players
'''
ball = random.choice(table)
def play_ball():

    print(f'{player_name} bets on {player_bet_numbers}')
    if ball in player_bet_numbers:
      print(f'Ball lands on {ball}. PLAYER WINS!!!')
    else:
        print(f'Ball lands on {ball}. House keeps the cash.')


'''==============================>>
Calculate payout
'''

def payout(amount, bet_type):
    
    if ball not in player_bet_numbers:
        player_payout = -1 * amount
    elif ball in player_bet_numbers and bet_type is 'reds' or 'blacks' or 'evens' or 'odds' or 'lows' or 'highs':
        player_payout = 0
    elif ball in player_bet_numbers and bet_type is 'dozens 1' or 'dozens 2' or 'dozens 3' or 'columns 1' or 'columns 2' or 'columns 3':
        player_payout = amount * 2
    elif ball in player_bet_numbers and bet_type is 'six line':
        player_payout = amount * 5
    elif ball in player_bet_numbers and bet_type is 'square':
        player_payout = amount * 8
    elif ball in player_bet_numbers and bet_type is 'street':
        player_payout = amount * 11
    elif ball in player_bet_numbers and bet_type is 'split' or 'zero row':
        player_payout = amount * 17
    elif ball in player_bet_numbers and bet_type is 'straight':
        player_payout = amount * 35
    
    print(f'{player_name} now has ${player_purse + player_payout} to play with.')
    
    return player_purse + player_payout

    

'''==============================>>
Play again OR End Game
'''
def play_again():
    re_bet = input(f'Would you like to place another bet? y/n:  ')
    if re_bet != 'y':
        print(f'Thanks for playing!')
    else:
        
        player_bet_type_inp = input('Select a type of bet from the above table. Enter Your Bet Type: ').lower()

        player_numbers(player_bet_type_inp, player_bet_numbers)

        player_bet_amount = int(input('How much would you like to bet? Enter Bet Amount: '))

        play_ball()
    
        payout(player_bet_amount, player_bet_type_inp)

def play_the_game ():
    
    roulette()
    bet_scheme()

    
    print(welcome_message)
    print(intro_message)

    

    player_bet_type_inp = input('Select a type of bet from the above table. Enter Your Bet Type: ').lower()

    player_numbers(player_bet_type_inp, player_bet_numbers)

    player_bet_amount = int(input('How much would you like to bet? Enter Bet Amount: '))

    play_ball()
    
    payout(player_bet_amount, player_bet_type_inp)

    play_again()

play_the_game()







    

