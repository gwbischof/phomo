from collections import Counter

def frequency_analysis(corpus):
    length = len(corpus)
    return {key: value/length for key, value in dict(Counter(corpus)).items()}
