"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return 'un'+word

# print(add_prefix_un("manageable"))
# print(add_prefix_un("happy"))

def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    A = []
    l = len(vocab_words)
    for i in range(1, l):
        wrd = vocab_words[0] + vocab_words[i]
        A.append(wrd)
    full_list = [vocab_words[0]] + A
    return ' :: '.join(full_list)

# print(make_word_groups(['pre', 'serve', 'dispose', 'position']))
# print(make_word_groups(['auto', 'didactic', 'graph', 'mate']))
# print(make_word_groups(['inter', 'twine', 'connected', 'dependent']))

def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    
    w = word[:-4]
    if w.endswith('i'):
        return w[:-1] + 'y'
    else:
        return w

# print(remove_suffix_ness("heaviness"))
# print(remove_suffix_ness("sadness"))

def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    a = sentence.split()
    w = a[index]
    w = w.strip(".,!")
    w = w + 'en'
    return w

# print(adjective_to_verb('I need to make that bright.', -1 ))
# print(adjective_to_verb('It got dark as the sun set.', 2))