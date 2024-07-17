def hand(card):
    """
    Function to evaluate the card based on its type and suit.
    :param card: Card object
    :return: score of the card and its description
    """
    suit_priority = {'Fire': 1, 'Earth': 2, 'Water': 3, 'Air': 4}
    type_priority = {'Knight': 1, 'Mage': 2, 'Ranger': 3}

    type_score = type_priority[card.card_type]
    suit_score = suit_priority[card.suit]
    
    # Higher type_score is better; if type_score is the same, higher suit_score is better
    score = type_score * 10 + suit_score
    description = f"{card.card_type} of {card.suit}"
    
    return score, description

def players_score(player_list):
    """
    Function calculates and assigns each player a score based on their selected card.
    :param player_list: list of players for whom scores are to be calculated
    :return: nothing, function assigns a score to player object
    """
    for player in player_list:
        if player.selected_card:
            score, description = hand(player.selected_card)
            player.score = score
            player.hand = description


def determine_winner(player1, player2):
    """
    Determine the winner based on RPS mechanics and suit priority.
    :param player1: AstraPlayer object
    :param player2: AstraPlayer object
    :return: winning player object or None if draw
    """
    type_priority = {'Knight': 1, 'Mage': 2, 'Ranger': 3}
    suit_priority = {'Fire': 1, 'Earth': 2, 'Water': 3, 'Air': 4}
    
    card1 = player1.selected_card
    card2 = player2.selected_card
    
    if type_priority[card1.card_type] - type_priority[card2.card_type] in [1, -2]:
        return player1
    elif type_priority[card2.card_type] - type_priority[card1.card_type] in [1, -2]:
        return player2
    else:
        if suit_priority[card1.suit] > suit_priority[card2.suit]:
            return player1
        elif suit_priority[card2.suit] > suit_priority[card1.suit]:
            return player2
        else:
            return None  # Draw


