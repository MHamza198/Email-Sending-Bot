import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Gmail account details
sender_email = 'michelmarsh88@gmail.com'  # Replace with your Gmail email
sender_password = 'Put your own'      # Replace with your Gmail password

# Email content
subject = ''
message = ''

def send_email_to_recipient(subject, message, recipient):
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

def load_recipients_from_excel(filename):
    try:
        df = pd.read_excel(filename)
        return df['Email'].tolist()
    except Exception as e:
        print(f"Error loading recipients from Excel: {e}")
        return []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        global subject, message
        subject = request.form['subject']
        message = request.form['message']
        recipient_file = request.files['file']
        if recipient_file:
            filename = os.path.join('uploads', recipient_file.filename)
            recipient_file.save(filename)
            recipient_list = load_recipients_from_excel(filename)
            for recipient in recipient_list:
                send_email_to_recipient(subject, message, recipient)
            os.remove(filename)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
