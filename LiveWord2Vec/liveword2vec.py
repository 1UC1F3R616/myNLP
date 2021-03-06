# -*- coding: utf-8 -*-
"""LiveWord2Vec.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gVtAW6LcIxhDlpwodnJKGCoTnzOgg0w9
"""

!pip install gensim
!pip install wikipedia

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from gensim.models import Word2Vec
import string
import warnings

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

import wikipedia
from wikipedia import search
from wikipedia import page

# Working with wikipedia
titles = search('Natural Language Processing')
# print(titles)
wikipage = page(titles[0])

# print(wikipage.content)
# print(wikipage.categories)

print(wikipedia.summary('Natural Language Processing', auto_suggest=True, ))

## Applying NLP
def preprocessing(text):
  result = []
  tokenized_sentences = sent_tokenize(text)
  for sentence in tokenized_sentences:
    tokenized_words = word_tokenize(sentence)
    stopwords_ = stopwords.words('english')
    filtered_tokenized_words = [word for word in tokenized_words \
                                if word.lower() not in string.punctuation \
                                and word.lower() not in stopwords_]
    lemma = WordNetLemmatizer()
    lemma_tokenized_words = [lemma.lemmatize(word) for word in filtered_tokenized_words]
    
    result += [lemma_tokenized_words]

  return result

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

text_p = preprocessing(wikipage.content)

print(text_p)

# Model
min_count = 2
size = 50
window = 4

wikimodel  = Word2Vec(text_p, min_count=min_count,  size=size, window=window)

# Result
vocab = list(wikimodel.wv.vocab.keys())
vocab[:10]
wikimodel.wv.most_similar(positive = ['learn', 'processing'], topn=3)

# wikimodel.wv.similarity('data', 'human') # similarity between this two