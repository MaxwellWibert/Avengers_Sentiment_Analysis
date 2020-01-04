import pickle
word_scores = pickle.load(open("./Resources/pickled_scores.p", "rb"))

def score(tweet):
    words = [word for word in tweet.split(" ") if word.isalpha()]
    tweetscore = 0
    for word in words:
        try:
            tweetscore += word_scores[word][2]
        except:
            continue
    return tweetscore