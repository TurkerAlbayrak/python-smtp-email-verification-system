import smtplib
import random
from email.mime.text import MIMEText

EMAIL = "SENDER_MAİL"
PASSWORD = "SENDER_MAİL_PASS"

def send_verification(email):
    code = str(random.randint(100000, 999999))

    msg = MIMEText(f"Doğrulama kodun: {code}")
    msg["Subject"] = "Doğrulama Kodu"
    msg["From"] = EMAIL
    msg["To"] = email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    server.send_message(msg)
    server.quit()

    return code
