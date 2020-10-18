import string
import random
import itertools
from collections import defaultdict


def generate_random_corpus(k=2, num_symbols=10, num_restrictions=5,
                           max_word_length=10, corpus_length=1000):

    def make_word(max_length, symbols, allowed_dictionary):
        # How long is the word going to be?
        length = random.randint(1, max_length)
        word = [random.choice(list(symbols))]
        for i in range(length-1):
            word.append(random.choice(list(allowed_dictionary[word[-1]])))

        # Converts the list to a string.
        word = ''.join([item for t in word for item in t])

        return word


    # TODO: Update letters with IPA symbols.
    letters = list(string.ascii_lowercase)
    symbols = set([random.choice(letters) for i in range(num_symbols)])

    symbol_permutations = list(itertools.permutations(symbols, 2))
    for symbol in symbols:
        symbol_permutations.append((symbol, symbol))

    restrictions = set([random.choice(symbol_permutations) for i in range(num_restrictions)])
    allowed = set(symbol_permutations) - set(restrictions)

    allowed_dictionary = defaultdict(set)   #each key's value is a default set
    for first, second in allowed:
        allowed_dictionary[first].add(second)
    allowed_dictionary = dict(allowed_dictionary)

    grammar = {"symbols":  (len(symbols), symbols),
               "restrictions":  (len(restrictions), restrictions),
               "allowed": (len(allowed), allowed),
               "allowed_dictionary": allowed_dictionary}

    corpus = " ".join([make_word(max_word_length, symbols, allowed_dictionary)
                      for i in range(corpus_length)])

    return grammar, corpus
