"""
Find the longest word in a pair and print its length.
The variables word1 and word2 are defined for you.
"""
# put your python code here

word1 = input()
word2 = input()

# How many letters does the longest word contain?
if len(word1) > len(word2):
    print(len(word1))
else:
    print(len(word2))