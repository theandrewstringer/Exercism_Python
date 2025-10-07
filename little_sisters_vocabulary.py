"""
Functions for creating, transforming, and adding prefixes to strings.
"""

def add_prefix_un(word):
    """
    Take the given word and add the 'un' prefix.
    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    # variable to store the required prefix
    prefix = 'un'

    # return the new word
    return prefix + word

def make_word_groups(vocab_words):
    """
    Transform a list containing a prefix and words into a string with the prefix 
    followed by the words with prefix prepended.
    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with prefix applied.
    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated by ' :: '.
    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    # set up the separator
    separator = ' :: ' + vocab_words[0]
    
    # return the new words with the prefix
    return separator.join(vocab_words)

def remove_suffix_ness(word):
    """
    Remove the suffix from the word while keeping spelling in mind.
    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.
    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    # check if the new word would end with an 'i'
    stem = word[:-4]
    
    # if the word would end with an 'i', change to 'y' and remove ness
    if stem.endswith('i'):
        return stem[:-1] + 'y'
    return stem

def adjective_to_verb(sentence, index):
    """
    Change the adjective within the sentence to a verb.
    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.
    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    # suffix that will be added
    suffix = 'en'

    #split the sentence into words
    words = sentence.split()

    # isolate the adjective
    adjective = words[index]

    # separate from trailing punctuation
    if adjective and not adjective[-1].isalnum():
        adjective = adjective[:-1]

    # verbify the adjective
    verbified = adjective + suffix
        
    # split the sentence to replace the adjective
    return verbified
