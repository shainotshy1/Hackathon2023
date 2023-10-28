from enum import Enum
from PyDictionary import PyDictionary

WordType = Enum('WordType', ['NONE', 'NOUN', 'VERB', 'ADJECTIVE', 'ADVERB', 'PREPOSITION'])
word_types = {"Noun":WordType.NOUN, 
              "Verb":WordType.VERB, 
              "Adjective":WordType.ADJECTIVE,
              "Adverb":WordType.ADVERB,
              "Preposition":WordType.PREPOSITION
              }

class WordDictionary:
    def __init__(self):
        self.words = {}
        self.dictionary = PyDictionary()

    @property
    def size(self):
        return len(self.words)
    
    def register(self, word, word_type):
        assert type(word_type) == list
        self.words[word] = word_type

    def get_types(self, word):
        if word not in self.words:
            meaning = self.dictionary.meaning(word, disable_errors=True)
            if meaning == None:
                self.register(word, [WordType.NONE])
            else:
                res = []
                word_keys = meaning.keys()
                assert len(word_keys) > 0, "word invalid"
                print(word_keys)
                for key in word_keys:
                    if key in word_types:
                        res.append(word_types[key])
                    else:
                        res.append(WordType.NONE) # word types that are not handled become none type
                self.register(word, res)
        return self.words[word]

class Sentence:
    def __init__(self, sentence, word_dictionary):
        self.text = sentence.split(' ')
        self.word_dictionary = word_dictionary

    def __str__(self):
        res = ""
        for i in range(self.size):
            res += self.word_at(i) + '{' + str(self.word_types_at(i)) + "}\n"
        return str(res)
        
    @property
    def size(self):
        return len(self.text)
    
    def word_at(self, i):
        return self.text[i]
    
    def word_types_at(self, i):
        return self.word_dictionary.get_types(self.word_at(i))