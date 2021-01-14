# import the libraries
from nltk.corpus import stopwords
# import nltk
# nltk.download('stopwords')

nltk_stopwords = stopwords.words('english')

# print(nltk_stopwords)

text = f"\nThe first time I saw Catherine she was wearing a vivid "\
       f"crimson dress and was nervously "\
       f"leafing through a magazine in my waiting room.\n"

# print(text)

text_without_stopword = [word for word in text.split() if word.lower() not in nltk_stopwords]

print(f"Original Text : {text}\n")
print(f"Text without stopwords : {' '.join(text_without_stopword)}\n")

print(f"Total count of stopwords in NLTK is {len(nltk_stopwords)}")