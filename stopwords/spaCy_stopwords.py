# import spacy library
import spacy

# python -m spacy download en_core_web_sm

sp = spacy.load('en_core_web_sm')
spacy_stopwords = sp.Defaults.stop_words

# print(spacy_stopwords)
# print(f"Total count of stopwords in SpaCy is {len(spacy_stopwords)}")


text = f"The first time I saw Catherine she was wearing a vivid " \
       f"crimson dress and was nervously " \
       f"leafing through a magazine in my waiting room."

text_without_stopword = [word for word in text.split() if word.lower() not in spacy_stopwords]

print(f"Original Text : {text}")

print(f"Text without stopwords : {' '.join(text_without_stopword)}")








