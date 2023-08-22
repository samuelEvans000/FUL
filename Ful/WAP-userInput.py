import requests
import re

def extract_info_from_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        content = response.text
        
        social_links = re.findall(r'href="(https?://www\.[a-zA-Z0-9.-]+)"', content)
        
        email_addresses = re.findall(r'[\w\.-]+@[\w\.-]+', content)
        
        contact_numbers = re.findall(r'\+\d{1,2}\s?\d{3}\s?\d{3}\s?\d{4}', content)
        
        return social_links, email_addresses, contact_numbers
    except Exception as e:
        print(f"An error occurred: {e}")
        return [], [], []

website_url = input("Enter the website URL: ")

social_links, email_addresses, contact_numbers = extract_info_from_website(website_url)

print("Social links -")
for link in social_links:
    print(link)

print("\nEmails:")
for email in email_addresses:
    print(email)

print("\nContact:")
for number in contact_numbers:
    print(number)
