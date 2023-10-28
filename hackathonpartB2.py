from PyDictionary import PyDictionary
dictionary=PyDictionary()

from random import random


class Pertubation:

    def __init__(self, sentenceDS):
        self.sentenceDS = sentenceDS

    def pert(self):
        for i in range(0, sentenceDS.types):
            synonyms = dictionary.synonym(sentenceDS.sentence[i])
            if sentenceDS.types[i] != "NONE":
                sentenceDS.sentence[i] = synonyms[random.randint(len(synonyms))]

        

    
    



