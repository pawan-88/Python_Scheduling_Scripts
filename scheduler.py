# This is Python Small script to scheadule a few APIs calls.

import requests
import datetime
import time
import threading
import logging
from typing import List

url = "https://ifconfig.co/"

# Basic loggegr setup – good enousgh for this smsall scripts.
logging.basicConfig(
    filename='Log.txt',
    level=logging.DEBUG,
    format='%(name)s: %(levelname)s - %(message)s - %(asctime)s.'
)

logger = logging.getLogger('Test')


#  Converts "HH:MM:SS" into a datetimes object.
def Formatting_Time(time_str: str) -> datetime.datetime:
    return datetime.datetime.strptime(time_str, "%H:%M:%S")


# Waitz until the given time string and then call the API once.
def Hitting_url(time_stamp):
    while True:
        now_str = datetime.datetime.now().strftime("%H:%M:%S")
        delay = (Formatting_Time(time_stamp) - Formatting_Time(now_str)).total_seconds()
        
        if delay <= 0:
            logger.info(f"Reached scheduled time, delay: {delay}")
            break

        time.sleep(min(delay, 1))
    
    try:
        logger.info("Time to hit the URL.")
        res = requests.get(url)

        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        
        if res.status_code == 200:
            print(f'Successful hit at {current_time}')
            logger.info("Success in hitting the URL")
        else:
            print(f"Unsuccessful in performing task at {current_time}")
            logger.warning(f"Status code issue. Status code: {res.status_code}")
    except Exception as e: # generic for catch original exception
        print("Exception occurred:", e)
        logger.error(f"Error whiles calling sthe API: {e}")

def main():
    user_input = input("Enter the timestamps (comma separated, HH:MM:SS): ")
    # Strip spaces and ignore empty chunks in case of trailing commas.
    time_stamps = [t.strip() for t in user_input.split(",") if t.strip()]
    print("Scheduled times:", time_stamps)
    
    for time_stamp in time_stamps:
        thread = threading.Thread(target=Hitting_url, args=(time_stamp,))
        thread.start()