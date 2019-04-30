from my_script import enlarge, notificationsigma

def test_enlarge():
    result = enlarge
    date = "xyz"
    assert result == "Tick-Tok Portfolio Management \nDate: " + date + "\nNone of your stocks had price movements that exceeded the threshold."

def test_notificationsigma():
    #message_count = 0
    #notification = "Tick-Tok Portfolio Management \n"

    #pctchg = 100
    #symbol = "AGR"
    #this value was replaced for running the pytest (not the actual value)




    #if ((pctchg*100) > threshold or (pctchg*100) < (threshold * -1)):
     #                   message_count += 1
      #                  output_pct_chg = "{0:,.2f}".format(pctchg*100)
       #                 notification += "\n" + f"     {symbol} moved {output_pct_chg}% today."
        #                return notificationsigma

        result = notificationsigma
        assert result == "AGR moved 100% today."

        
def test_sheet_log():
    result = sheet_log
    assert result == "0123456789"
