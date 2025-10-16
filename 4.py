import re

text = "Hello world From Python Regex"
matches = re.findall(r'[A-Z][a-z]+', text)
print(matches)
