from email.message import EmailMessage
import ssl
import smtplib
#import schedule // still testing functionality on schedule send
#import time

email_sender = "your.email@provider.com" # use email you'd like to send the message from.
app_password = "[enter app password here]" #Insert 16-digit App password code found in 2-step verification section of Gmail. Redacted for security purposes. 
email_receiver = "your.email@provider.com" # use email you'd like to send message to.

subject = "insert subject here"
body = """
insert body text here
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)


context = ssl.create_default_context()


with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as smtp:
    smtp.login(email_sender, app_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

# Schedule the job to run daily at a specific time (adjust as needed)
#schedule.every().day.at("08:00").do(send_email)

#while True:
    #schedule.run_pending()
    #time.sleep(1)
