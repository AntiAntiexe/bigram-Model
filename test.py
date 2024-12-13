from collections import Counter

# Given corpus
corpus = ['GeeksforGeeks is', 'is a', 'a great', 'great learning', 'learning platform', 'platform .', '. It', 'It is', 'is one', 'one of', 'of the', 'the best', 'best for', 'for Computer', 'Computer Science', 'Science students', 'students .']

# Flatten the list of strings into a list of words
words = ' '.join(corpus).split()

print(words)

# Count the frequency of each word
word_counts = Counter(words)

# Total number of words
total_words = sum(word_counts.values())

# Calculate the probability of each word
word_probabilities = {word: count / total_words for word, count in word_counts.items()}

# Print the probabilities
for word, probability in word_probabilities.items():
    print(f"{word}: {probability:.4f}")
