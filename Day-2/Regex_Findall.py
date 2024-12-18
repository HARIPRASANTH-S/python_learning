import re

text = "Rose is red in Colour"
pattern = r'is'

search = re.search(pattern, text)

if search:
    print('Found', search.group())
else:
    print('Not Found')