import re


def calculateAverage(sentence):
    sentence = re.sub(r'[^a-zA-Z\d\s]', u' ', sentence, flags=re.UNICODE)
    sentence = re.split(' ', sentence)
    sentence = list(filter(None, sentence))
    wordLen = 0
    for word in sentence:
        if word != '':
            wordLen = wordLen + len(word)
    return round((wordLen / len(sentence)), 2)
