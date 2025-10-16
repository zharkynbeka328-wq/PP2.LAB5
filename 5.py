import re

pattern = r'a.*b$'
test_strings = ['a123b', 'ab', 'acccb', 'a-b', 'abc']
for s in test_strings:
    if re.fullmatch(pattern, s):
        print(s)
