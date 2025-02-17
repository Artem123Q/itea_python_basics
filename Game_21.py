'''Create a game - 21.
There are 10 cards representing values 2-11.
The goal is to get max points, but less then 21. Each turn a player should decide pick a new card o pass.
Pick - value of a card should be added to player's points. If player gets more then 21 points - he lost.
Pass - no new cards, player stays with current points.
Results should be shown only after all the players passed.

Level 1 - one player.
Level 2 - one player + one bot.
Level 3 - one player + two bots.

To generate a random card use:
from random import randint
randint(2, 11)
Added by medviediev'''
from random import randint
card_value_1 = randint(2, 11)
card_value_2 = randint(2, 11)
player_score = 0
bot_score = 0
player_start_cards = randint(2, 11) + randint(2, 11)
bot_start_cards = randint(2, 11) + randint(2, 11)
player_points = player_start_cards + player_score
bot_points = bot_start_cards + bot_score

if player_start_cards >= 21 > bot_start_cards:
    print('You Winner!!!! You get 21 point in the start', 'Player score: ', 21)
elif player_start_cards < 21 <= bot_start_cards:
    print('You Loose!!!! Bot get 21 point in the start', 'Bot score: ', 21)
elif player_start_cards and bot_start_cards >= 21:
    print('Draw', 'Bot score = Player score: ', 21)
    # You should not continue game, because smaller amount of cards win!
else:
    while True:
        bot_get_card = randint(0, 1)
        if bot_get_card == 1:
            bot_score += randint(2, 11)
            bot_points = bot_start_cards + bot_score
            continue
        get_card = input('Do you wont to pick a card?\n write \"Pick\" or \"Pass\"')
        if get_card == 'Pick':
            player_score += randint(2, 11)
            player_points = player_start_cards + player_score
            if player_points < 21:
                continue
            elif player_points == 21:
                print('User Points:', player_points)
                print('Bot Points:', bot_points)
                if bot_points == 21:
                    print('Draw')
                else:
                    print('Player win!')
                    break
            elif player_points > 21:
                print('User Points:', player_points)
                print('Bot Points:', bot_points)
                if bot_points <= 21:
                    print('Bot win!')
                else:
                    print('Draw')
                break
        if get_card == 'Pass' or bot_get_card == 0:
            print('User Points:', player_points)
            print('Bot Points:', bot_points)
            if bot_points == 21:
                print('Bot win!')
            elif bot_points > 21:
                print('Player win!')
            elif bot_points == player_points:
                print('Draw')
            elif player_points < 21:
                if player_points < bot_points:
                    print('Bot win!')
                else:
                    print('Player win!')
            break