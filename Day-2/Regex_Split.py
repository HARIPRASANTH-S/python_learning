import re

text = 'a,b,c,d'
pattern = r','

split = re.split(pattern, text)
print(split)
