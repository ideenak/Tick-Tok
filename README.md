# Tick Tok Portfolio Management Tool

1. clone this repo and download dependencies
```
git clone https://github.com/ideenak/Tick-Tok

cd Tick-Tok

pip install -r requirements.txt
```

2. Request an API key from https://www.alphavantage.co/ 
```
touch .env
Open .env file and insert ```ALPHAVANTAGE_API_KEY='YOUR API KEY GOES HERE'``` 
```

3. Download Google Sheets and Google Drive api credentials from https://cloud.google.com/apis/

```
Replace api credentials file in /auth with new downloaded credentials
```

4. Request an API Key and Authorization Token from https://www.twilio.com/
```
touch .env
Open .env file and insert ```account_sid='YOUR API KEY GOES HERE'``` and ```auth_token ='YOUR AUTHORIZATION TOKEN GOES HERE'```

```

5. Create google form to gather portfolio information and google sheet to store data
```
Share the google sheet with the email address under "client email" in the google api credential file
Update the SHEET_NAME in app/final.py 
Update the GOOGLE_SHEET_ID in the .env
```

6. Gather information from the google form 
```
Share the google sheet with the email address under "client email" in the google api credential file
```

7. Run the file

```
python robo_advisor.py
Program will send messages to the numbers entered in the google sheet
```

