from phomo import a, b, generate_random_corpus

def test_ab():
    assert a() == b() 

"""
def test_classifier():
    corpus1 = generate_random_corpus()
    corpus2 = generate_random_corpus()

    training_data = corpus1_slice + corpus2_slice
    test_data = corpus1_slice2 + corpus2_slice2

    classifier = train_classifier(training_data)
    
    accuracy = classifier.classify(test_data)

    print(accuracy)
"""
