import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Gmail account details
sender_email = 'muhammadhamza198198@gmail.com'
sender_password = 'wjwlgfcucorbkfjg'

# Recipient list
recipient_list = ['hamzashahzad198@gmail.com', 'muhammadhamza198198198@gmail.com']

# Email content
subject = 'Your Subject'
message = 'Your Message'

def send_email(subject, message, recipient):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient, msg.as_string())
        server.quit()
        print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Error sending email to {recipient}: {e}")

# Sending emails to recipients
for recipient in recipient_list:
    send_email(subject, message, recipient)
