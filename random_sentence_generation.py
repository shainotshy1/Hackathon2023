#importing yay
import random

import spacy

from PyDictionary import PyDictionary
import random

dictionary = PyDictionary()
nlp = spacy.load("en_core_web_sm")

# Define parts of speech and sentence structure rules
#make these libraries later on
nouns = ["cat", "dog", "ball", "house"]
verbs = ["runs", "jumps", "barks", "sleeps"]
articles = ["The", "A"]
adjectives = ["quick", "lazy", "big", "small"]
adverbs=["quickly","slowly","lazily","tiredly"]
pronouns_subjects=["I","he","she","it"]

placeholders = ["{article}", "{noun}", "{adjective}", "{verb}", "{adverb}","{adjective}"]

# Define sentence structure templates
sentence_structures = [
    "{article} {noun} {verb}.",
    "{article} {adjective} {noun} {verb}.",
    "{article} {noun} {verb} {adverb}.",
    "Haha,{pronouns_subject} {verb} {adverb}"
    "{article}{noun} {verb} {article}.",
    "Wow,{pronouns_subject} {verb} {noun}.",
    "{article} {noun} {verb} in {article} {adjective} {noun}.",
    "Did you know {pronouns_subject} {verb} with {article} {noun}.",
    "{article} {adjective} {noun} {verb} {adverb}.",
    "{article} {adjective} {noun} {verb} at night.",
    "{article} {noun} is {adjective}.",
    "{article} {noun} {verb} {article} {adjective}.",
    "It's {adjective} and {adjective}.",
    "Hey,{pronouns_subject} {verb} because the {noun} is too {adjective}."
]
# Shuffle word lists to avoid repetition
random.shuffle(nouns)
random.shuffle(verbs)
random.shuffle(articles)
random.shuffle(adjectives)
random.shuffle(adverbs)

# ... Rest of your code ...

# Generate a random sentence structure
def generate_random_structure():
    structure = random.choice(sentence_structures)
    return structure.format(
        article=articles.pop(),
        noun=nouns.pop(),
        adjective=adjectives.pop(),
        verb=verbs.pop(),
        pronouns_subject=pronouns_subjects.pop(),
        adverb=adverbs.pop()
    )

# Function to generate a sentence based on an example input

# Function to generate a sentence based on an example input
def generate_sentence_from_example(example_sentence):
    # Tokenize the example sentence
    tokens = example_sentence.split()
    sentence_structure = " ".join(placeholders)

    for i, token in enumerate(tokens):
        if token in placeholders:
            placeholder = token[1:-1]  # Remove curly braces
            if placeholder in placeholders:
                word_list = placeholders[placeholder]
                if i < len(tokens) - 1 and tokens[i + 1] in placeholders:
                    # If the next token is also a placeholder, replace with a random word
                    sentence_structure = sentence_structure.replace(token, random.choice(word_list), 1)
                else:
                    # If the next token is not a placeholder, replace with a synonym or antonym
                    word = word_list.pop()
                    synonym = dictionary.synonym(word)
                    antonym = dictionary.antonym(word)
                    replacement = random.choice([word, synonym, antonym])
                    sentence_structure = sentence_structure.replace(token, replacement, 1)

    return sentence_structure #returns modified sentence with placeholders to then be replaced

# Another function to replace remaining placeholders and create a complete sentence
def create_complete_sentence(sentence_structure):
    # Tokenize the sentence structure
    tokens = sentence_structure.split()

    # Initialize a dictionary to map placeholders to corresponding word lists
    placeholder_mapping = {
        "{article}": articles,
        "{noun}": nouns,
        "{adjective}": adjectives,
        "{verb}": verbs,
        "{adverb}": adverbs,
        "{pronouns_subject}": pronouns_subjects
    }

    # Replace remaining placeholders with words
    complete_sentence = []
    for token in tokens:
        if token in placeholder_mapping:
            # Replace the placeholder with a random word from the corresponding word list
            word = random.choice(placeholder_mapping[token])
            complete_sentence.append(word)
        else:
            # Keep non-placeholder tokens as they are
            complete_sentence.append(token)

    # Join the tokens to form the complete sentence
    complete_sentence = " ".join(complete_sentence)

    return complete_sentence

# Main program
user_choice = input("Do you want to generate a sentence based on an example input? (yes/no): ")
if user_choice.lower() == "yes":
    example_sentence = input("Enter an example sentence: ")
    generated_sentence = generate_sentence_from_example(example_sentence)
    complete_sentence = create_complete_sentence(generated_sentence)  # Process the returned sentence structure
    print(complete_sentence)
else:
    random_structure = generate_random_structure()
    print(random_structure)

# Main program
user_choice = input("Do you want to generate a sentence based on an example input? (yes/no) (choose no for random generative feature): ")
if user_choice.lower() == "yes":
    example_sentence = input("Enter an example sentence: ")
    generated_sentence = generate_sentence_from_example(example_sentence)
    print(generated_sentence)

#else as default for random generation
else:
    random_structure = generate_random_structure()
    print(random_structure)
