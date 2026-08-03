import os
import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import pytz

# -----------------------------------
# Google API Scopes
# -----------------------------------
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# -----------------------------------
# Connect to Google Sheet
# -----------------------------------
def get_sheet():

    # Local Development
    if os.path.exists("creds/service_account.json"):

        credentials = Credentials.from_service_account_file(
            "creds/service_account.json",
            scopes=SCOPES
        )

    # Streamlit Cloud
    else:

        credentials = Credentials.from_service_account_info(
            st.secrets["gcp_service_account"],
            scopes=SCOPES
        )

    client = gspread.authorize(credentials)

    sheet = client.open("Expense Tracker").sheet1

    return sheet


# -----------------------------------
# Add Expense
# -----------------------------------
# Indian Time Zone
IST = pytz.timezone("Asia/Kolkata")

def add_expense(amount, description):

    sheet = get_sheet()

    now = datetime.now(IST)

    today = now.strftime("%d-%m-%Y")
    current_time = now.strftime("%I:%M %p")

    sheet.append_row([
        today,
        current_time,
        amount,
        description,
        "",
        ""
    ])
