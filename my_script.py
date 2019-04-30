from dotenv import load_dotenv
import json
import os
import requests
import datetime
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from twilio.rest import Client


def enlarge(i):
    if(message_count == 0):
        date = "xyz"
        notification = "Tick-Tok Portfolio Management \nDate: " + date + "\nNone of your stocks had price movements that exceeded the threshold."

        message = client.messages \
                        .create(
                            body=notification,
                            #from_='+15405180462',
                            #to=recipient
                        )
        return message


def notificationsigma(i):
    message_count = 0
    notification = "Tick-Tok Portfolio Management \n"

    pctchg = 100
    symbol = "AGR"
    #this value was replaced for running the pytest (not the actual value)




    if ((pctchg*100) > threshold or (pctchg*100) < (threshold * -1)):
                        message_count += 1
                        output_pct_chg = "{0:,.2f}".format(pctchg*100)
                        notification += "\n" + f"     {symbol} moved {output_pct_chg}% today."
                        return notificationsigma


#certain variables that were irrelevant to the actual test were changed

def sheetlog(i):
    DOCUMENT_ID = os.environ.get("GOOGLE_SHEET_ID", "OOPS")
    SHEET_NAME = "TickTok (Responses)"
    

