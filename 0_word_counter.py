from collections import Counter
import sys
import re

count = Counter(word 
                for line in sys.stdin
                for word in re.split('[^A-Za-z0-9]+', line.lower())
                if word)

for word, freq in count.most_common(1000):
    sys.stdout.write(word)
    sys.stdout.write("\t")
    sys.stdout.write(str(freq))
    sys.stdout.write("\n")