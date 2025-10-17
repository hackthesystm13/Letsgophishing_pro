import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests

# Temporary email service configuration
temp_email_service = 'https://www.10minutemail.com/'

def get_temp_email():
    response = requests.get(temp_email_service)
    # Parse the response to extract the temporary email address
    # This will depend on the structure of the HTML response
    # For demonstration, we'll use a placeholder email address
    return 'temp_email@example.com'

def send_email(to, body, from_email=None):
    if from_email is None:
        from_email = get_temp_email()
    from_password = 'temp_password'  # Temporary passwords are usually not required

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to
    msg['Subject'] = 'Important Update'

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    text = msg.as_string()
    server.sendmail(from_email, to, text)
    server.quit()
    print(f"Email sent to {to} from {from_email}")