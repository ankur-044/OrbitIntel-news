import os

print("Generating OrbitIntel Report...")
os.system("python generate_report.py")

print("Creating PDF...")
os.system("python pdf_test.py")

print("Sending Emails...")
os.system("python send_email.py")

print("OrbitIntel Daily Automation Completed.")