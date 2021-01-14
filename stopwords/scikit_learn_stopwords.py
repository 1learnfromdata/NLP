# import scikit-learn libraries
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

# print(ENGLISH_STOP_WORDS)
# print(f"Total count of stopwords in Sklearn is {len(ENGLISH_STOP_WORDS)}")

text = f"The first time I saw Catherine she was wearing a vivid crimson "\
       f"dress and was nervously " \
       f"leafing through a magazine in my waiting room."

text_without_stopword = [word for word in text.split() if word.lower() not in ENGLISH_STOP_WORDS]

print(f"Original Text : {text}\n")

print(f"Text without stopwords : {' '.join(text_without_stopword)}")

# add stopwords into list

stopwords_total = list(ENGLISH_STOP_WORDS)
stopwords_total.remove('the')

text_without_stopword = [word for word in text.split() if word.lower() not in stopwords_total]

print(f"Original Text : {text}\n")

print(f"Text without stopwords : {' '.join(text_without_stopword)}")


