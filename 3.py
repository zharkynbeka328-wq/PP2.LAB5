import re

text = "first_name lastName some_variable_name anotherOne"
matches = re.findall(r'[a-z]+_[a-z]+', text)
print(matches)
