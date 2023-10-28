from PyDictionary import PyDictionary
dictionary = PyDictionary()

def splitting(sentence):
    sentence = sentence.split(' ')
    return sentence

# limit sentences by category

def obtainKey(desiredKey):
    # list out keys and values separately
    # key represents a string of a specific word and val represents the string of what type it is: noun, verb, adjective
    key_list = list(dictionary.keys())
    val_list = list(dictionary.values())
 
    # print key with val 100
    for i in key_list:
        x = 0
        if i == desiredKey: 
            position = val_list[x]
        else:
            x += 1

    return key_list[position]