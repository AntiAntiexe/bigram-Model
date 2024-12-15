from nltk import word_tokenize, sent_tokenize
from collections import Counter
import re

class App:
    def __init__(self):
        self.sent = "GeeksforGeeks is a great learning platform. \
                It is one of the best for Computer Science students. And it is really fun. And it is really intuitive."
        self.file1 = open("newnew.txt","r+")
        self.sent = self.file1.read()
        self.sent = self.sent.lower()
        print(self.sent)
        #print(word_tokenize(self.sent))
        self.sent_list = word_tokenize(self.sent)
        self.words = []

        for i in range(len(word_tokenize(self.sent))):
            try: 
                self.words.append(self.sent_list[i] +' '+ self.sent_list[i+1])
                #print(self.words)
            except: 
                 print('Index out of range')

    

    def counter(self):
        # Count the frequency of each word
        self.word_counts = Counter(self.words)

        # Total number of words
        self.total_words = sum(self.word_counts.values())

        #print(self.total_words)

        # Calculate the probability of each word
        self.word_probabilities = {word: count / self.total_words for word, count in self.word_counts.items()}

        print(self.word_probabilities.items())

        # Print the probabilities
        for word, probability in self.word_probabilities.items():
            print(f"{word}: {probability:.4f}")
        
        word_Input = input('Enter a word for the bigram model: \n')
        probs = []
        for word, probability in self.word_probabilities.items():
            x = ''.join(word).split()
            if word_Input == x[0]:
                print('That word can be predicted using the corpus')
                probs.append(f'{word,probability}')

            #else:
                #print('cont')
        def strip_nonalnum_re(word):
            return re.sub(r"^\W+|\W+$", "", word)
        
        print(probs)

        correct_prob = max(probs)
        print(correct_prob.split())

        #x_word = strip_nonalnum_re(''.join(correct_prob).split()[1])
        x_word = ''.join(correct_prob).split()[1]
        print(word_Input, x_word)

      
App().counter()