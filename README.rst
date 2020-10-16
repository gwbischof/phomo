=====
phomo
=====

.. image:: https://img.shields.io/travis/yangliustonybrook/phomo.svg
        :target: https://travis-ci.org/yangliustonybrook/phomo

.. image:: https://img.shields.io/pypi/v/phomo.svg
        :target: https://pypi.python.org/pypi/phomo


code about grammar generator (phonology)
========================================
- Step 0: to randomly generate a grammar
- Step 1: to generate an artificial corpus using the grammar
- Step 2: to extract/calculate a grammar from the artificial corpus
- Step 3: to compare the calculated grammar and the original grammar
- Assumption: Restrictions are only length 2, and local.

# Problem: the length of corpus could affect the accuracy of the calculated restrctions; How to statistically calculate the confidence?

# To do:
- Evaluate a word's well-formedness under the calculated restrictions.
- Generalize the functions to extend the range of applicable grammars (k = n, non-local/distant restrictions)
- auto-correction/completion of syllables, words

# input: syllable/word output: a classified language
 - transducer

# output: acceptance rating of a certain syllable/word
- compare the output accuracy of feature&rule-based learner and purely frequency-based learner

phonology models and relevant interfaces

* Free software: 3-clause BSD license
* Documentation: (COMING SOON!) https://yangliustonybrook.github.io/phomo.

Features
--------

* TODO
