import random

from player import Player
from auction import auction
from score import players_score
from utils import recap_round, split_pot, one_player_win, change_players_positions
from constants import SB, BB


def poker_round():
    """
    Function play one round of dealing cards.
    """

    # In player_list players order will change after each round
    player_list_chair = Player.player_list_chair
    player_list = Player.player_list

    # Take blinds from players
    if player_list[-1].stack > BB:
        player_list[-1].blind(BB)
    else:
        player_list[-1].blind(player_list[-1].stack)
        player_list[-1].allin()

    if player_list[-2].stack > SB:
        player_list[-2].blind(SB)
    else:
        player_list[-2].blind(player_list[-2].stack)
        player_list[-2].allin()

    # Create a deck of cards
    deck = ['MB', 'MG', 'MR', 'MY', 'KB', 'KG', 'KR', 'KY', 'RB', 'RG', 'RR', 'RY']

    # Deal the cards to the player
    for player in player_list_chair:
        player.cards = random.sample(deck, 3)
        [deck.remove(player.cards[i]) for i in range(3)]

    # First auction
    auction()

    # Check how many players are in the game and all-in
    number_live_players = sum([player.live for player in player_list])
    number_allin_players = sum([player.alin for player in player_list])

    # change order decision player
    if len(player_list_chair) == 2:
        shift_decision = -1
    else:
        shift_decision = -2

    # If there is only one player left in the game, he wins
    if number_live_players + number_allin_players == 1:
        list_winner = one_player_win()
        recap_round(list_winner)
    else:
        # Flop
        flop = random.sample(deck, 3)
        [deck.remove(flop[i]) for i in range(3)]

        # Change order decision players
        change_players_positions(shift_decision)

        if number_live_players > 1:
            # Second auction
            auction(flop)

        # Check how many players are in the game and all-in
        number_live_players = sum([player.live for player in player_list])
        number_allin_players = sum([player.alin for player in player_list])

        # If there is only one player left in the game, he wins
        if number_live_players + number_allin_players == 1:
            list_winner = one_player_win()
            recap_round(list_winner)
            # Return to the original position
            change_players_positions(shift_decision)
        else:
            # Deal the cards to the turn
            turn = random.sample(deck, 1)
            deck.remove(turn[0])
            common_cards = flop + turn

            if number_live_players > 1:
                # Third auction
                auction(common_cards)

            # Check how many players are in the game and all-in
            number_live_players = sum([player.live for player in player_list])
            number_allin_players = sum([player.alin for player in player_list])

            # If there is only one player left in the game, he wins
            if number_live_players + number_allin_players == 1:
                list_winner = one_player_win()
                recap_round(list_winner)
                # Return to the original position
                change_players_positions(shift_decision)
            else:

                # Deal the cards to the river
                river = random.sample(deck, 1)
                deck.remove(river[0])
                common_cards += river

                if number_live_players > 1:
                    # Last auction
                    auction(common_cards)

                # Check how many players are in the game and all-in
                number_live_players = sum([player.live for player in player_list])
                number_allin_players = sum([player.alin for player in player_list])

                # If there is only one player left in the game, he wins
                if number_live_players + number_allin_players == 1:
                    list_winner = one_player_win()
                    recap_round(list_winner)
                    # Return to the original position
                    change_players_positions(shift_decision)
                else:
                    # Calculate score players
                    players_score(player_list_chair)
                    # Split pot
                    list_winner = split_pot()
                    recap_round(list_winner, common_cards)
                    # Return players to the original position
                    change_players_positions(shift_decision)


