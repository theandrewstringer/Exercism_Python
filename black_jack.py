"""
Functions to help play and score a game of blackjack.
How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

# define face cards and numbered cards
face_cards = {'J': 10, 'Q': 10, 'K': 10, 'A': 1}
numbered_cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, 
                      '7': 7, '8': 8, '9': 9, '10': 10}

def value_of_card(card):
    """
    Determine the scoring value of a card.
    :param card: str - given card.
    :return: int - value of a given card.  See below for values.
    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    
    # combine dictionaries for ease of use and then look up the value
    all_cards = {**face_cards, **numbered_cards}
    return all_cards.get(card)

def higher_card(card_one, card_two):
    """
    Determine which card has a higher value in the hand.
    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.
    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    # create variables for comparison, and call previous function
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
        
    # compare values
    if value_one > value_two:
        return card_one
    elif value_one < value_two:
        return card_two
    else:
        return (card_one, card_two)

def value_of_ace(card_one, card_two):
    """
    Calculate the most advantageous value for the ace card.
    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.
    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    # create variables
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    # determine if an ace is already in hand, and return what value a drawn ace should be
    if value_one == 1 or value_two == 1:
        return 1
    elif value_one + value_two > 10:
        return 1
    else:
        return 11

def is_blackjack(card_one, card_two):
    """
    Determine if the hand is a 'natural' or 'blackjack'.
    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).
    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    # create variables
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    # check if there is an ace in hand and if so, if there is a face card or 10
    if value_one == 1 or value_two == 1:
        if value_one == 10 or value_two == 10:
            return True
        else:
            return False
    else:
        return False

def can_split_pairs(card_one, card_two):
    """
    Determine if a player can split their hand into two hands.
    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    # create variables
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    # determine if you can split cards
    return value_one == value_two

def can_double_down(card_one, card_two):
    """
    Determine if a blackjack player can place a double down bet.
    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    # create variables
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    # define double down values
    double_down_values = [9, 10, 11]

    # determine if you can double down
    return value_one + value_two in double_down_values
