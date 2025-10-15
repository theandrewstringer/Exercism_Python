"""
Functions for tracking poker hands and assorted card tasks.
Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""

def get_rounds(number):
    """
    Create a list containing the current and next two round numbers.
    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    # define the rounds variable and return the list
    rounds = [number, number + 1, number + 2]
    return rounds

def concatenate_rounds(rounds_1, rounds_2):
    """
    Concatenate two lists of round numbers.
    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    # create total rounds variable and return the concatenated list
    total_rounds = rounds_1 + rounds_2
    return total_rounds

def list_contains_round(rounds, number):
    """
    Check if the list of rounds contains the specified number.
    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    # determine if the number is in the rounds
    if number in rounds:
        return True
    return False
        
def card_average(hand):
    """
    Calculate and returns the average card value from the list.
    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    # create a variable for the number of cards in the hand
    count = len(hand)

    # sum the hand
    total = sum(hand)

    # return the average
    return total / count

def approx_average_is_average(hand):
    """
    Return if the (average of first and last card values) OR ('middle' card) == calculated average.
    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    # average of first and last card values
    sum_first_last = hand[0] + hand[-1]
    avg_first_last = sum_first_last / 2

    # find the average of the hand
    count = len(hand)
    total = sum(hand)
    avg_hand = total / count

    # find the median
    median = count // 2

    # determine if either of the two strategies works
    if avg_hand in (avg_first_last, hand[median]):
        return True
    return False

def average_even_is_average_odd(hand):
    """
    Return if the (average of even indexed card values) == (average of odd indexed card values).
    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    # find the average of the even indexes
    count_even = len(hand[::2])
    sum_even = sum(hand[::2])
    avg_even = sum_even / count_even

    # find the average of the odd indexes
    count_odd = len(hand[1::2])
    sum_odd = sum(hand[1::2])
    avg_odd = sum_odd / count_odd

    # determine if the avg of the even indexes is the same as the avg of the odd indexes
    if avg_even == avg_odd:
        return True
    return False

def maybe_double_last(hand):
    """
    Multiply a Jack card value in the last index position by 2.
    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    # check for jack and double if so, then return hand
    if hand[-1] == 11:
        hand[-1] *= 2
        return hand
    return hand
