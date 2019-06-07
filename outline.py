import re

f = open("seneca_falls.txt", "r")
wordlist = f.read()

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

wordlist = wordlist.lower()
wordlist = re.sub(r'[^a-z]', " ", wordlist)
wordlist = wordlist.split()
# print(wordlist)

# now the text file is split into individual words, all lowercase

di = {}
clean_wordlist = []
for w in wordlist:
    if w not in STOP_WORDS:
        clean_wordlist.append(w)
# print(clean_wordlist)

for w in clean_wordlist:
    di[w] = di.get(w,0) + 1
# print(di)

sorted(di, key=di.__getitem__)

print(di)


# may have to convert to tuple?

# di[w] declares w as the key. the right of equals is incrementing the value. above is both declaring the key and the method of counting the value in the dictionary

# have to use key to sort by the number of times word appears