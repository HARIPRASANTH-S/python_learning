import re

text = "Rose is a beautifull flower"
pattern = r'Rose'

replace = 'Lily'

search = re.search(pattern, text)
if search:
    newtext = re.sub(pattern, replace, text)
    print("New Text : ", newtext)
else:
    print("No CHnage : ", text)
