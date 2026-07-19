from datetime import datetime
import pandas as pd
import requests

# current date & time
now = datetime.now()

# get day
current_day = now.strftime("%A")

# get time
current_time = now.time()

# get excel table
df = pd.read_excel(r"C:\Users\Shree\Desktop\PYTHON\AUTOMATION PROJECT\Airtel Espace MSC Automation\Cleaning Message Schedule Espace MSC.xlsx")

# get the matching row
today_cleaning = df[
    (df["Day"] == current_day) &
    (df["Start Time"] <= current_time) &
    (df["End Time"] >= current_time)
]

# send the message to target telegram group
if today_cleaning.empty:
    print("No cleaning scheduled now")
else:
    message = today_cleaning.iloc[0]["Message"]

    TOKEN = ""
    CHAT_ID = ""

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    response = requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": message
        }
    )
    

   