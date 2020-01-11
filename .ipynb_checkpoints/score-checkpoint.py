import pickle
import string
word_scores = pickle.load(open("./Resources/pickled_scores.p", "rb"))



def score(text):
    words = [word.translate(str.maketrans('', '', string.punctuation)).lower() for word in text.split(" ")]
    text_score = 0
    for word in words:
        try:
            text_score += word_scores[word][2]
        except:
            continue
    return text_score

def normal_score(text):
    words = [word.translate(str.maketrans('', '', string.punctuation)).lower() for word in text.split(" ")]
    return score(text)/len(words)