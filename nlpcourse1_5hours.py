# -*- coding: utf-8 -*-
"""NLPcourse1.5Hours.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/180e3yvtDZvTq_h-56KsS4OrSk3phyyC7

## Tokenize
- word
- sentence
"""

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

dataset = 'Hi My dataset is created by Me. Lol I know'
dataset2 = """Hello Mr. Watson, how are you doing today?
             The weather is awsome. The garden is green.
             We should go out for a walk."""

import nltk
nltk.download('punkt')

print(sent_tokenize(dataset))
print(sent_tokenize(dataset2))

print(word_tokenize(dataset))
print(word_tokenize(dataset2))

"""## Stop Words
- search engines are programmed to ignore the Stop Words
"""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
print(stop_words)

words = word_tokenize(dataset)
filtered_words = []
for word in word_tokenize(dataset):
  if word not in stop_words:
    filtered_words.append(word)

print(filtered_words)

"""## Stemming -
The process of removing prefixes, suffixes from the words and reduce them to their stem form.

For example, the word "computation" might be stemmed to "comput"

- Porter Stemming - The most common algorithm used for stemming in English,
It consists of several phases of word reductions that are applied sequentially.
"""

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

dataset3 = ['love', 'lover', 'loving', 'loved', 'lovingly']

for w in dataset3:
  print(ps.stem(w))

"""## Tagging
- Automatic assignment of descriptors to the given tokens is called Tagging
- Tagging is a kind of classification

### POS (Parts-Of-Speech) Tagging
- The process of assigning one of the parts of a speech to the given word is POS tagging [noun, pronoun, verb, adverb, preposition, conjective, adjective, interjection] 
- eg. word:paper, tag:noun

- POS tagger is a program that does the job of POS tagging
- Taggers use several kinds of information: dictionaries, lexicons, rules
There are mainly two types of taggers rule-based and stochastic
  - Rule-bases tagger:
     - Hand-writtem rules to distinguish
  - Stochastic taggers
    - HMM based
    - likelihood of the word, tag sequence probability
    - decision trees and maximum entropy
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

nltk.download('averaged_perceptron_tagger')
nltk.download('tagsets')

pos_tag(word_tokenize(dataset))

nltk.help.upenn_tagset()

"""## Chunking
- like we don't memorise a phone nnumber as seprate individual numbers, we group them together to memorise easily
- chunking is grouping of information
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import RegexpParser

tokenized_data = word_tokenize(dataset)
pos_tagging = pos_tag(tokenized_data)

chunk_sequence = """
chunk:
{<NNPS>+}
{<NNP>+}
{<NN>}"""

chunk = RegexpParser(chunk_sequence)

chunked_data = chunk.parse(pos_tagging)
print(chunked_data)

"""## Named Entity Recognition
- Also known as
  - Entity Identification
  - Entity Chunking
  - Entity Extraction
- It is a subtask of information extraction that classify named entities into pre-defined categories such as names of persons, organizations, locations
- Tesla: Organization, Elon Musk: Person

### Applications
- classify the contents to news providers
- Efficent search Algorithms
- Content recommendation
- Question and Answer systems
- Automatic Forwarding
- Online document searching
"""

from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk

tagged_data = pos_tag(word_tokenize(dataset))

nltk.download('maxent_ne_chunker')
nltk.download('words')

# Applying Named Entity Recognization with ne_chunk
ne_data = ne_chunk(tagged_data)
print(ne_data)

# won't work on GC
# ne_data.draw()

"""## Lemmatization
- Process of converting the words of a sentence into it's dictionary form.
word: Feet, Lemma: Foot
  - we get a meaningful name
  
## Stemming
- Process of converting the words of a sentence to it's non-changing portions
  - we may or may not get a meaningful name
"""

from nltk.stem import WordNetLemmatizer

wnl = WordNetLemmatizer()

nltk.download('wordnet')

words = ['dogs', 'cars', 'feet', 'people']
for word in words:
  print(wnl.lemmatize(word))

print(wnl.lemmatize('fantasized', 'v'))

"""## Corpus
- Large collection of text
- spoken material on which liguistic analysis is based
"""

import nltk

nltk.download('state_union')
from nltk.corpus import state_union

dataset = state_union.raw('2001-GWBush-1.txt')

"""## Wordnet
- Lexical database in english language
- It group english words in antonyms and synonyms
- Also provides short examples and words
"""

from nltk.corpus import wordnet

syns = wordnet.synsets('program')
print(syns)

print(syns[0].lemmas())
print(syns[0].lemmas()[0].name()) # Getting the name of it
print(syns[0].lemmas()[1].name())

# Getting the meaning of that word
print(syns[0].definition())

print(syns[0].examples())

# Antonyms
antonyms = []
synonyms = []

for syn in wordnet.synsets('good'):
  for l in syn.lemmas():
    synonyms.append(l.name())
    if l.antonyms():
      antonyms.append(l.antonyms()[0].name())

print(antonyms)
print(synonyms)