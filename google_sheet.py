import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

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

    credentials = Credentials.from_service_account_file(
        "creds/service_account.json",
        scopes=SCOPES
    )

    client = gspread.authorize(credentials)

    sheet = client.open("Expense Tracker").sheet1

    return sheet


# -----------------------------------
# Add Expense
# -----------------------------------
def add_expense(amount, description):

    sheet = get_sheet()

    today = datetime.now().strftime("%d-%m-%Y")
    current_time = datetime.now().strftime("%I:%M %p")

    sheet.append_row([
        today,
        current_time,
        amount,
        description,
        "",
        ""
    ])
