import re

def is_valid_contact_number(num):
    
    pattern = r'^(\+\d{1,2})?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,10}$'
    
    if re.match(pattern, num):
        return True
    else:
        return False

test_nums = [
    "2124567890",
    "212-456-7890",
    "(212)456-7890",
    "(212)-456-7890",
    "212.456.7890",
    "212 456 7890",
    "+12124567890",
    "+12124567890",
    "+1 212.456.7890",
    "+212-456-7890",
    "1-212-456-7890"
]

for num in test_nums:
    if is_valid_contact_number(num):
        print(f"{num} is a valid contact number.")
    else:
        print(f"{num} is an invalid contact number.")
