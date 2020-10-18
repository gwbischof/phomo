from collections import Counter

def frequency_analysis(corpus):
    length = len(corpus)
    return {key: value/length for key, value in dict(Counter(corpus)).items()}


'''
class Classifier():
    """
    Just defining the API for classifiers.
    """

    def __init__(self, corpus_dict):
    """
    Input
    =====
    corpus_dict: dict
        Maps class-label (language) to training corpus.
    """

    def classify(self, sample):
        return class_label
'''

class FrequencyClassifier():

    def __init__(self, corpus_dict):
        self._train(corpus_dict)

    def _train(self, corpus_dict):
        self._models = {language: frequency_analysis(corpus)
                       for language, corpus in corpus_dict.items()}

    def _compare(self, language_model, sample):
        frequency_analysis(sample)
        # TODO: compare sample and language model frequencies.
        # Return a float between 0 and 1. Where 0 means that they are identical.
        return 0.5

    def classify(self, sample):
        best_result = 2
        best_language = None
        for language, model in self._models.items():
            result = self._compare(model, sample)
            if result < best_result:
                best_result = result
                best_language = language
        return best_language


"""
cd = {'lang1': corpus1,
      'lang2': corpus2}
"""
