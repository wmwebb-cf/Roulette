"""
WELCOME TO THE BIG WHEEL'S CASINO & CABARET

Tasks:
[] Set up the table with proper numbers
[] 
"""

import random
#dice_one = random.randint(0, 36)


'''
setup table spaces
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


"""
ball played
"""

ball = random.choice(zero_spot['zero'] + red_spot['red'] + black_spot['black'])

'''
Determine what spot the ball landed on
'''


if ball in [x for y in zero_spot.values() for x in y]:
    print(f'ball lands on GREEN: {ball}')
elif ball in [x for y in red_spot.values() for x in y]:
    print(f'ball lands on RED: {ball}')
elif ball in [x for y in black_spot.values() for x in y]:
    print(f'ball lands on BLACK: {ball}')

    

