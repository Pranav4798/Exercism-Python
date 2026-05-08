


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    l = []
    for i in range(3):
        l.append(number)
        number = number+1
        

    return l

# print(get_rounds(27))

def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2

# print(concatenate_rounds([27, 28, 29], [35, 36]))


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    if number in rounds:
        return True
    else:
        return False
        
# print(list_contains_round([27, 28, 29, 35, 36], 29))
# print(list_contains_round([27, 28, 29, 35, 36], 30))


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    sum = 0
    for i in range(len(hand)):
        sum += hand[i]

    avg = sum/len(hand)

    return avg

# print(card_average([5, 6, 7]))

import math

def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    act_avg = sum(hand) / len(hand)
    avg_first_last = (hand[0] + hand[-1])/2
    median = hand[len(hand)//2]

    return act_avg == avg_first_last or act_avg == median

# print(approx_average_is_average([1, 2, 3]))
# print(approx_average_is_average([1, 2, 3, 5, 9]))
# print(approx_average_is_average([2, 3, 4, 8, 8]))

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    l = len(hand)
    e = []
    o = []

    for i in range(l):
        if i%2 == 0:
            e.append(hand[i])
        else:
            o.append(hand[i])

    even = sum(e)/len(e)
    odd = sum(o)/len(o)

    if even == odd:
        return True
    else:
        return False

# print(average_even_is_average_odd([1, 2, 3]))
# print(average_even_is_average_odd([1, 2, 3, 4]))

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = hand[-1] + hand[-1]
        return hand
    else:
        return hand

# print(maybe_double_last([5,9,11]))
# print(maybe_double_last([5,9,10]))