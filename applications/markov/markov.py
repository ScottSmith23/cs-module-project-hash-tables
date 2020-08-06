import random

##pseudocode
#       1. read text
    #split into words
    #   2. Analyze the text, which words can follow a word
    #   3. any word at index + 1



# Read in all the words in one go
with open("applications/markov/input.txt") as f:
    s = f.read()

    #split words
    cache = {}

    #remove specific characters
# for char in '":;,.-+=/\\|[]{}()*^&?!':  
#     s = s.replace(char,'')


# TODO: analyze which words can follow other words
# Your code here

    split_words = s.split()
for i in range(len(split_words) - 1):
    word = split_words[i]
    next_word = split_words[i + 1]

    if word not in cache:
        cache[word] = [next_word]

    else:
        cache[word].append(next_word)

start_words = []
for key in cache.keys():
    if key[0].isupper() or len(key) > 1 and key[1].isupper():
        start_words.append(key)

word = random.choice(start_words)


# TODO: construct 5 random sentences
# Your code here


counter = 0
stop_signs ="?.!"

while counter != 5:
    #print word
    print(word, end=' ')

    #stop at a stop word
    if word[-1] in stop_signs or len(word) > 1 and word[-2] in stop_signs:
        counter += 1
        print('\n')
    #choose a random word to follow
    following_word = cache[word]

    word = random.choice(following_word)
