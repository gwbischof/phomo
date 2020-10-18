from phomo.generate import generate_random_corpus
from phomo.statistics import frequency_analysis

def test_frequency_analysis():
    grammar, corpus = generate_random_corpus()
    print(frequency_analysis(corpus))
