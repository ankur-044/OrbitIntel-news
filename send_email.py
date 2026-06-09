import pandas as pd
import yagmail
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Read secrets from .env
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

# Load client list
clients = pd.read_csv("clients.csv")

# Connect to Gmail
yag = yagmail.SMTP(
    user=SENDER_EMAIL,
    password=APP_PASSWORD
)

# Send emails
for _, row in clients.iterrows():

    yag.send(
        to=row["email"],
        subject="OrbitIntel AI Daily Space Intelligence",
        contents="""
Hello,

Attached is today's OrbitIntel AI Space Intelligence Report.

Regards,
OrbitIntel AI
""",
        attachments="output.pdf"
    )

    print(f"Email sent to {row['email']}")

print("All emails sent successfully.")