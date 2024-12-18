import re

text = "is red in Colour"
pattern = r'is'

match = re.match(pattern, text)

if match:
    print('found', match.group())
else:
    print('Not FOund')
