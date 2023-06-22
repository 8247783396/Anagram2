"""Anagram Grouping"""

words = input().split()
words = set(words)
d = {}

for word in words:
    char_counts = [0] * 26

    for char in word:
        index = ord(char) - ord('a')
        char_counts[index] += 1
    
    key = tuple(char_counts)

    if key not in d:
        d[key]=[word]

    else:
        d[key].append(word)

anagram_groups = list(d.values())
print(anagram_groups)
