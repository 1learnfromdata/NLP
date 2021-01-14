# import genism libraries
from gensim.parsing.preprocessing import remove_stopwords
import gensim
gensim_stopwords = gensim.parsing.preprocessing.STOPWORDS

# print(gensim_stopwords)
# print(f"Total count of stopwords in Gensim is {len(list(gensim_stopwords))}")

text = f"The first time I saw Catherine she was wearing a vivid "\
       f"crimson dress and was nervously " \
       f"leafing through a magazine in my waiting room."

print(f"Original Text : {text}\n")

print(f"Text without stopwords : {remove_stopwords(text.lower())}")

# print(f"Total count of stopwords in Gensim is {len(list(gensim_stopwords))}")