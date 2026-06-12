"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed.

    :param title: str - title string that needs title casing.
    :return: str - title string in title case (first letters capitalized).
    """

    return title.title()

# print(capitalize_title("my hobbies"))

def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present.

    :param sentence: str - a sentence to check.
    :return: bool - return True if punctuated correctly with period, False otherwise.
    """

    if sentence.endswith('.'):
        return True
    return False

# print(check_sentence_ending("I like to hike, bake, and read."))
# print(check_sentence_ending("I am a disco dancer"))
# print(check_sentence_ending("Mitochondria is powerhouse"))
# print(check_sentence_ending("Rise of Krypton."))

def clean_up_spacing(sentence):
    """Verify that there isn't any whitespace at the start and end of the sentence.

    :param sentence: str - a sentence to clean of leading and trailing space characters.
    :return: str - a sentence that has been cleaned of leading and trailing space characters.
    """

    return sentence.strip()
    
# print(clean_up_spacing(" I like to go on hikes with my dog.  "))
# print(clean_up_spacing("  Small steps everyday   "))
# print(clean_up_spacing("    You are a good man Arthur Morgan   "))
# print(clean_up_spacing("Hii   this is a   Wendys"))

def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.
    :param sentence: str - a sentence to replace words in.
    :param old_word: str - word to replace.
    :param new_word: str - replacement word.
    :return: str - input sentence with new words in place of old words.
    """

    word = sentence.replace(old_word, new_word)
    return word

# print(replace_word_choice("I bake good cakes.", "good", "amazing"))
# print(replace_word_choice("I bake good cakes.", "good", "the best"))
# print(replace_word_choice("Take me higher", "higher", "lower"))
