# import libraries
from nltk.corpus import stopwords
import spacy
import gensim
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

nltk_stopwords = set(stopwords.words('english'))

sp = spacy.load('en_core_web_sm')
spacy_stopwords = sp.Defaults.stop_words

gensim_stopwords = gensim.parsing.preprocessing.STOPWORDS

print(list(nltk_stopwords))
print(list(spacy_stopwords))
print(list(gensim_stopwords))
print(list(ENGLISH_STOP_WORDS))


