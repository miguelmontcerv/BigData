# def mapper(input: str):
#     line = input.strip()
#     words = line.split()
#
#     result = ""
#     for word in words:
#         result += '%s\t%s\n' % (word, 1)
#
#     return result


import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()

    for word in words:
        print('%s\t%s\n' % (word, 1))