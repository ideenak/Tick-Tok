from dotenv import load_dotenv
import json
import os
import requests
import datetime
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from twilio.rest import Client



load_dotenv() # loads environment variables set in a ".env" file, including the value of the ALPHAVANTAGE_API_KEY variable

api_key = os.environ.get("ALPHAVANTAGE_API_KEY") 

CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "auth", "google_api_credentials.json")

DOCUMENT_ID = os.environ.get("GOOGLE_SHEET_ID", "OOPS")
SHEET_NAME = "TickTok (Responses)"

AUTH_SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
    "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
]

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)

client = gspread.authorize(credentials) #> <class 'gspread.client.Client'>

doc = client.open_by_key(DOCUMENT_ID)

print(SHEET_NAME)
print(api_key)
print(DOCUMENT_ID)



sheet = doc.worksheet(SHEET_NAME)

rows = sheet.get_all_records() #> obtaining information, row by row, from the google sheet, storing it in a list of dictionaries

for row in rows:
    print("-------")
    print("NEW ROW")

    ##CLIENT INFO
    name = row["Name"]
    phone_number = row["Phone Number"]
    threshold = int(row["Threshold Preference"])
    print("Name: " + str(name))
    print("Phone Number: " + str(phone_number))
    print("Threshold: " + str(threshold))

    #VALIDATING TICKER INFO
    print("------------")
    print("stock info:")


    i = 1
    message_count = 0
    notification = "Tick-Tok Portfolio Management \n"
    date_and_notice_included = 0
    date = ""

    while i < 6:
        symbol = row[f"Stock {i}"]
        if(symbol != ""):
            request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
            stock_info = requests.get(request_url)
            if("Error" in stock_info.text): #> Checking for error in the stock ticker symbol
                print(f"error in Stock {i}")
            else:
                parsed_stock_info = json.loads(stock_info.text) #> Loading parsed alpha vantage json info into list of dictionaries
                latest_day = parsed_stock_info['Meta Data']['3. Last Refreshed']
                latest_day = latest_day[:10]
                date = latest_day
                latest_day_opening_price = float(parsed_stock_info['Time Series (Daily)'][latest_day]['1. open'])
                latest_day_closing_price = float(parsed_stock_info['Time Series (Daily)'][latest_day]['4. close'])
                print("opening: " + str(latest_day_opening_price))
                print("closing: " + str(latest_day_closing_price))

                if(date_and_notice_included == 0): 
                    notification += "Date: " + latest_day
                    notification += "\nNotice:"
                    date_and_notice_included = 1

                ##checking price movement

                pct = threshold/100

                gthresh = (1 + pct) * float(latest_day_opening_price)
                lthresh = (1 - pct) * float(latest_day_opening_price)

                pctchg = ((latest_day_closing_price - latest_day_opening_price)/latest_day_opening_price) #> calculating % change in price to be used in checking against threshold

                print("% change: " + str(pctchg * 100))

                if ((pctchg*100) > threshold or (pctchg*100) < (threshold * -1)):
                    message_count += 1
                    output_pct_chg = "{0:,.2f}".format(pctchg*100)
                    notification += "\n" + f"     {symbol} moved {output_pct_chg}% today."


        i += 1


    account_sid = str(os.environ.get('account_sid')) #> obtaining twilio keys and authorization
    auth_token = str(os.environ.get('auth_token'))
    client = Client(account_sid, auth_token)

    recipient = "+1" + str(phone_number)

    if(message_count == 0): #> changing to default message if no stocks moved above the threshold level
        notification = "Tick-Tok Portfolio Management \nDate: " + date + "\nNone of your stocks had price movements that exceeded the threshold."

    message = client.messages \ #> sending message
                    .create(
                        body=notification,
                        from_='+15405180462',
                        to=recipient
                    )
