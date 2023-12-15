from dotenv import load_dotenv
from email.message import EmailMessage
import requests
import os
import smtplib
import random

'''
The select() randomly picks a quote category and return it.
'''


def select(choice):
    random_category = choice[random.randint(0, len(choice) - 1)]
    return random_category


'''
The fetch_quote() function fetches a quote from https://api-ninjas.com/api/quotes and returns a .json data list. 
'''


def fetch_quote():
    category = ["attitude", "Computers", "courage", "dreams", "failure", "forgiveness", "freedom", "friendship",
                "happiness", "hope", "imagination", "inspirational", "leadership", "morning", "success"]
    api_url = f"https://api.api-ninjas.com/v1/quotes?category={select(category)}"
    quote_response = requests.get(api_url, headers={"X-Api-Key": os.getenv("QUOTE_API")})
    if quote_response.status_code == requests.codes.ok:
        return quote_response.json()  # Put the data in .json format
    else:
        print(quote_response.status_code, quote_response.text)


"""
The codes below sends the email 
"""

# Load variables from .env file
load_dotenv()

# Set up sender's and receiver's email address and password and hide them in an .env file
sender_email = os.getenv("EMAIL_ADDRESS")  # EMAIL_ADDRESS and EMAIL_PASSWORD are stored in .env
sender_password = os.getenv("EMAIL_PASSWORD")
receiver_email = os.getenv("RECEIVER")

# Email Content
subject = "Good Morning Tao!!!"
quote = fetch_quote()
text = "There's an error loading the quote :("
try:
    text = f"Quote of the Day: {quote[0].get('quote')}\n\nAuthor: {quote[0].get('author')}"
except Exception as e:
    print(f"Error While Formatting the Quote: {e}")

content = f"How Are You Doing Today?\n\n{text}"

# Create the email message
message = EmailMessage()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject
message.set_content(content)

# Send the Email
server = smtplib.SMTP("smtp.gmail.com", 587)  # Create a smtplib.SMTP object and connect with gmail's SMTP server
server.starttls()  # Establish TLS secure communication
server.login(sender_email, sender_password)  # Actually authenticated the script
server.send_message(message)
server.quit()
print("Email Has Been Sent to " + receiver_email)
