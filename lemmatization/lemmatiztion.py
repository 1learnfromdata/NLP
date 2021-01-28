from nltk.stem import WordNetLemmatizer
# import nltk 
# nltk.download('wordnet') 
lemmatizer = WordNetLemmatizer()

example_text = """kites,babies,dogs,flying,smiling,driving,died,tried,feet"""  
[print(lemmatizer.lemmatize(word)) for word in example_text.split(',')]

text = f" He determined to drop his litigation with the monastery , and relinquish"\
    f" his claims to the wood cutting and fishery rights at once . "\
    f"He was more ready to do this ."


text_without_stopword = [lemmatizer.lemmatize(word) for word in text.split()]
print(f"Original text: {text} \n")
print(f"Lemmetazied text : {' '.join(text_without_stopword)}")
