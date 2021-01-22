import nltk
porter_stemmer = nltk.PorterStemmer()


# example_text = """likes   liked likely begin begun began  smile smiled Jumping Jumped	Jump"""
# [print(porter_stemmer.stem(word)) for word in example_text.split()]


# text = f" He determined to drop his litigation with the monastery, and relinquish"\
#     f" his claims to the wood cutting and fishery rights at once. "\
#     f"He was more ready to do this."
# text_without_stopword = [porter_stemmer.stem(word) for word in text.split()]
# print(f"Original text: {text} \n")
# print(f"Stemmed text : {' '.join(text_without_stopword)}")

snowball_stemmer = nltk.SnowballStemmer('english')
example_text = """likes   liked likely begin begun began  smile smiled Jumping Jumped	Jump"""
[print(porter_stemmer.stem(word)) for word in example_text.split()]

text = f" He determined to drop his litigation with the monastery , and relinquish"\
    f" his claims to the wood cutting and fishery rights at once . "\
    f"He was more ready to do this . "
text_without_stopword = [snowball_stemmer.stem(word) for word in text.split()]
print(f"Original text: {text} \n")
print(f"Stemmed text : {' '.join(text_without_stopword)}")