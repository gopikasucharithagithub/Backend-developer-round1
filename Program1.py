import re

phone_regex = '^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$'
phone_number = '(212)-456-7890'
match = re.search(phone_regex, phone_number)

print(match)

