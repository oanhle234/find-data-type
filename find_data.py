import re

print('Enter any character or string')
text = input()
print('Your text: ', text)

# Find and print number list in text
number = re.findall(r'[0-9]', text)
print('Number: ', number)

# Find and print number list in the form of money ($45, 45$, 45 VND, 45 USD)
money = re.findall(r'\d+\$|\$\d+|\d+USD|\d+VND', text)
print('Money: ', money)

# Find and print email list
email = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', text)
print('Email: ', email)

# Find and print upper case list
upper_case = re.findall(r'[A-Z]', text)
print('Upper case: ', upper_case)
