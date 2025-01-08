import smtplib # Importing the smtplib module for sending emails
import ssl     # Importing the ssl module for secure connections
from email.message import EmailMessage # Importing the EmailMessage class to create email content


sender_email = "sender_email@gmail.com"      # Replace with your email address
receiver_email = "receiver_email@gmail.com"  # Replace with receiver email address
subject = "Automated Email Sender Project"
body = """This is an Automated Email Sender Project using Python.
	  The project allows you to send automated emails with custom content, all from within Python.
          I used Gmail's SMTP server and secured the connection using SSL"""

# Create a new email message
message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
# message.set_content(body)     # To send plain text content of the email instead of HTML format

# Creating an HTML version of the email content if you like to send email in HTML format
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>{subject}</h1>
    <p>{body}</p>
</body>
</html> """

message.add_alternative(html, subtype = "html") # Adding the HTML version as an alternative
connection = ssl.create_default_context()       # Create an SSL context for secure connection

while True:
    App_password = input("Enter App Password : ") # App password (16-character),not your account password

    try:
        print("Sending Email...")  # Inform user that the email is being sent

        # Create a secure SMTP connection using SSL
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=connection) as server: 
            server.login(sender_email, App_password) # Attempt login
            server.sendmail(sender_email, receiver_email, message.as_string()) # Send the email
        print("Message Sent :)")  # Inform user that the email was sent successfully
        break  # Exit the loop if the email was sent successfully

    except smtplib.SMTPAuthenticationError:
        print("Incorrect App Password. Please try again.")  # Error message for wrong password

    except smtplib.SMTPRecipientsRefused:
        print("Invalid Email Address. Please check and try again.") # Error message for Invalid Email Address 
  
