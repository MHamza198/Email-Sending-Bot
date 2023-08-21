import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd

# Gmail account details
sender_email = 'muhammadhamza198198@gmail.com'  # Replace with your Gmail email
sender_password = 'wjwlgfcucorbkfjg'      # Replace with your Gmail password

# Load recipient email addresses from Excel file
def load_recipients_from_excel(filename):
    try:
        df = pd.read_excel(filename)
        return df['Email'].tolist()
    except Exception as e:
        print(f"Error loading recipients from Excel: {e}")
        return []

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

# Load recipient emails from Excel file
recipient_file = 'recipient_list.xlsx'  # Replace with your Excel file name
recipient_list = load_recipients_from_excel(recipient_file)

# Sending emails to recipients
for recipient in recipient_list:
    send_email(subject, message, recipient)
