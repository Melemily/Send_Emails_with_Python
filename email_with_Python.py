from email.message import EmailMessage
import ssl
import smtplib

email_sender = "melphil.business@gmail.com"
email_password = "" #Insert 16-digit App password code found in 2-step verification section of Gmail. Redacted for security purposes. 
email_receiver = "ikebukuro.blonde@gmail.com"

subject = "Check out my cool email!"
body = """
I've just created this email with Python!
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)


context = ssl.create_default_context()


with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
