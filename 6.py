import re

text = "Python, is great. Really great language"
result = re.sub(r'[ ,.]', ':', text)
print(result)
