import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def select_random_email():
    html = """
    <html>
      <body>
        <p>Hello!</p>
        <p>Monday we are gonna work like hell week. There is so much</p>
      </body>
    </html>
    """

    return (subject, html)

def send_email(
        sender_email = "pankaj@testube.in",
        receiver_email = "pankaj@testube.in",
        password = "USXJoh(1",
        
        smtp_server = "us2.smtp.mailhostbox.com",
        smtp_port = 587
    ):
    # Set up the email parameters
    message = MIMEMultipart("alternative")
    message["Subject"], html = select_random_email()
    message["From"] = sender_email
    message["To"] = receiver_email
    message['Disposition-Notification-To'] = sender_email

    # Convert the HTML to a MIMEText object
    body = MIMEText(html, "html")

    # Attach the body to the message and send the email
    message.attach(body)

    # Choose the appropriate SMTP server and smtp_port for your email provider
    # if "gmail" in sender_email:
    #     smtp_server = "smtp.gmail.com"
    #     smtp_port = 465
    # elif "yahoo" in sender_email:
    #     smtp_server = "smtp.mail.yahoo.com"
    #     smtp_port = 587
    # elif "hotmail" in sender_email or "outlook" in sender_email:
    #     smtp_server = "smtp.office365.com"
    #     smtp_port = 587
    # elif "testube" in sender_email:
    #     smtp_server = "us2.smtp.mailhostbox.com"
    #     smtp_port = 587
    # else:
    #     raise ValueError("Unsupported email provider")

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.ehlo()
        if smtp_port == 587:
            server.starttls()
            server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


if __name__ == "__main__":
    send_email()