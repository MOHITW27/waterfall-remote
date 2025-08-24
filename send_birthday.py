import pandas as pd
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import os

# Load Excel file
df = pd.read_excel("Birthdays.xlsx")

# Get today's month-day
today = datetime.today().strftime("%m-%d")

# Email credentials
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))

# Loop through rows
for _, row in df.iterrows():
    bday = pd.to_datetime(row["Birthday"]).strftime("%m-%d")
    if bday == today:
        to_email = row["Email"]
        name = row["Name"]

        # 🎂 Hosted image URL (replace with your repo image or CDN)
        birthday_image = "https://github.com/MOHITW27/waterfall-remote/blob/master/Happy_Birthday_Image.JPG"

        # HTML Email Content
        subject = "🎉 Happy Birthday from Nokia!"
        body = f"""
        <html>
        <head>
          <style>
            body {{
              font-family: Arial, sans-serif;
              background-color: #f4f6f8;
              margin: 0;
              padding: 0;
            }}
            .container {{
              max-width: 600px;
              margin: 20px auto;
              background: #ffffff;
              border-radius: 10px;
              box-shadow: 0 2px 6px rgba(0,0,0,0.1);
              overflow: hidden;
            }}
            .header {{
              background-color: #124191;
              color: white;
              padding: 20px;
              text-align: center;
              font-size: 22px;
              font-weight: bold;
            }}
            .content {{
              padding: 30px;
              color: #333333;
              font-size: 16px;
              line-height: 1.6;
              text-align: center;
            }}
            .content img {{
              max-width: 200px;
              margin-bottom: 20px;
            }}
            .footer {{
              background-color: #f1f1f1;
              text-align: center;
              padding: 15px;
              font-size: 13px;
              color: #666666;
            }}
          </style>
        </head>
        <body>
          <div class="container">
            <div class="header">
              🎂 Happy Birthday, {name}!
            </div>
            <div class="content">
              <img src="{birthday_image}" alt="Birthday Celebration" />
              <p>Dear {name},</p>
              <p>Wishing you a <b>wonderful birthday</b> filled with joy, happiness, and success. 🥳</p>
              <p>May this year bring you new opportunities, exciting challenges, and memorable moments.</p>
              <p>Enjoy your special day!</p>
              <p>— Your Nokia Family 💙</p>
            </div>
            <div class="footer">
              Nokia · Connecting People
            </div>
          </div>
        </body>
        </html>
        """

        msg = MIMEText(body, "html")
        msg["Subject"] = subject
        msg["From"] = EMAIL_USER
        msg["To"] = to_email

        # Send email
        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(EMAIL_USER, EMAIL_PASS)
                server.sendmail(EMAIL_USER, to_email, msg.as_string())
            print(f"✅ Birthday email sent to {name} ({to_email})")
        except Exception as e:
            print(f"❌ Failed to send email to {to_email}: {e}")



