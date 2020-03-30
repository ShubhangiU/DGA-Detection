# import these modules 
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import tldextract

ps = PorterStemmer()

# choose some words to be stemmed
ext = tldextract.extract('http://forums.news.cnn.com/')
words = ["alexa", "google", "facebook", "programing", "programers"]
list = ext.domain
words.append(list)
print(words)
for w in words:
    print(w, " : ", ps.stem(w))