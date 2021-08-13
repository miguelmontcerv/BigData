import sys

current_word = None
current_count = 0
word = ""

for line in sys.stdin:
    line = line.strip()
    word, count = line.split("\t", 1)

    count = int(count)

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print('%s\t%s\n' % (current_word, current_count))
        current_count = count
        current_word = word