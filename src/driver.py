"""
A simple driver script to verify operation.
"""

from wordRank import WordRank

# Create two WordRank objects, one that excludes stopwords and one that doesn't.
print("Creating testobj1 with exclude_stopwords = True.\n")
testobj1 = WordRank(file_name="../input/MobyDick_Chapter1.txt", exclude_stopwords=True)
print("Creating testobj2 with exclude_stopwords = False.\n")
testobj2 = WordRank(file_name="../input/MobyDick_Chapter1.txt", exclude_stopwords=False)
print("Attempting creation of testobj3 with non-utf8 file.\n")
try:
    testobj3 = WordRank(file_name="../input/non_utf8_file.txt")
except UnicodeDecodeError:
    print("Unicode decode error encountered attempting to open 'non_utf8_file.txt'.\n")

# The total number of words read should be the same regardless of stopwords.
print(f"Total words read from MobyDick_Chapter1.txt: {testobj1.get_total_words()}.\n")

# Verify that default iterator behavior works.
x = {x: testobj1[x] for x in testobj1}

# Check some values.
print(f"Number of times 'ishmael' occurred in file: {x['ishmael']}.\n")
print(f"Count for 'and' in testobj1: {testobj1['and']}.\n")
print(f"Count for 'and' in testobj2: {testobj2['and']}.\n")
print(f"Non-stopwords that occurred 10 times in the file: {testobj1[10]}.\n")
print(f"All words that occurred 10 times in the file: {testobj2[10]}.\n")

print("\nTop 10 words excluding stopwords:")
i = 0
for rank, word in testobj1.get_rankings():
    i += 1
    if i > 9:
        break
    print(word + " " + str(rank))

print("\nTop 10 words including stopwords:")
i = 0
for rank, word in testobj2.get_rankings():
    i += 1
    if i > 9:
        break
    print(word + " " + str(rank))
