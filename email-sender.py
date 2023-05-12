import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email credentials
sender_email = "pankajlookingjobs@gmail.com"
sender_password = "quad2core"
receiver_email = "805.bluebell@gmail.com"

# Create message object instance
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'Test email'

# Email body
message.attach(MIMEText('Hello, this is a test email!'))

# Set up SMTP server
smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()

# Log in to SMTP server
smtp_server.login(sender_email, sender_password)

# Send email
smtp_server.sendmail(sender_email, receiver_email, message.as_string())
print("Email sent successfully!")
smtp_server.quit()
