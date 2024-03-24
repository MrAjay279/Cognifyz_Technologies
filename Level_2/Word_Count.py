def count_word_occurrences(file_path):
    word_counts = {}

    # Open the file and read its contents
    with open(file_path, 'r') as file:
        # Read each line of the file
        for line in file:
            # Tokenize the words
            words = line.split()
            for word in words:
                # Remove punctuation marks and convert to lowercase
                word = word.strip('.,!?').lower()
                # Update word count
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

    return word_counts

def display_word_counts(word_counts):
    # Sort word counts alphabetically
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[0])

    # Display word counts
    for word, count in sorted_word_counts:
        print(f"{word}: {count}")

# Path to the text file
file_path = "sample.txt"  

# Count word occurrences
word_counts = count_word_occurrences(file_path)

# Display word counts in alphabetical order
print("Occurrences of each word in alphabetical order:")
display_word_counts(word_counts)
