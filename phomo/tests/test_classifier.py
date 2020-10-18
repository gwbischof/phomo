from phomo.generate import generate_random_corpus
from phomo.statistics import FrequencyClassifier

def test_frequency_classifier():
    corpus_dict = {'lang1': generate_random_corpus()[1],
                   'lang2': generate_random_corpus()[1]}
    sample = corpus_dict['lang1'][0:500]
    frequency_classifier = FrequencyClassifier(corpus_dict)
    assert frequency_classifier.classify(sample) == 'lang1'
