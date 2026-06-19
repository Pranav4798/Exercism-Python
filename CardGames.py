"""Module providing a function printing python version."""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    card_tot = []
    for rounds in range(1,4):
        card_tot.append(number + rounds - 1)

    return card_tot

def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    if number in rounds:
        return True
    return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    sum_hand = 0
    for num_card, card in enumerate(hand):
        sum_hand += hand[num_card]

    avg = sum_hand/len(hand)

    return avg


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    act_avg = sum(hand) / len(hand)
    avg_first_last = (hand[0] + hand[-1])/2
    median = hand[len(hand)//2]

    return act_avg in {avg_first_last, median}


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    len_hand = len(hand)
    even_crd = []
    odd_crd = []

    for card_val in range(len_hand):
        if card_val%2 == 0:
            even_crd.append(hand[card_val])
        else:
            odd_crd.append(hand[card_val])

    even = sum(even_crd)/len(even_crd)
    odd = sum(odd_crd)/len(odd_crd)

    if even == odd:
        return True
    return False


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = hand[-1] + hand[-1]
        return hand
    return hand
