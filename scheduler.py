# This is Python Small script to scheadule a few APIs calls.
import datetime
import time
import threading
import logging
import requests


url = "https://ifconfig.co/"

# Basic loggegr setup – good enousgh for this smsall scripts.
logging.basicConfig(
    filename='Log.txt',
    level=logging.INFO,
    format="%(message)s",
    force=True
)

logger = logging.getLogger('Test')


#  Converts "HH:MM:SS" into datetimes object.
def Formatting_Time(time_str: str) -> datetime.datetime:
    today = datetime.datetime.now().date()
    t = datetime.datetime.strptime(time_str, "%H:%M:%S").time()
    return datetime.datetime.combine(today, t)

# Waitz until the given time string and then call the API once.
def Hitting_url(time_stamp):
    target_time = Formatting_Time(time_stamp)

    delay = (target_time - datetime.datetime.now()).total_seconds()

    if delay > 0:
        time.sleep(delay)

    # Log immediately when scheduled time is reached
    hit_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_time = target_time.strftime("%Y-%m-%d %H:%M:%S")

    #logger.info(f"Hitting API at scheduled time {log_time}, actual time {hit_time}")

    try:
        res = requests.get(url)

        if res.status_code == 200:
            print(f"Successful hit at {hit_time}")
            logger.info(f"{log_time} Success in hitting the URL {url}")
        else:
            print(f"Unsuccessful hit at {hit_time}")
            logger.warning(f"Status code issue: {res.status_code}")

    except Exception as e:
        logger.error(f"Error while calling API: {e}")

def main():
    user_input = input("Enter the timestamps (comma separated, HH:MM:SS): ")
    # Strip spaces and ignore empty chunks in case of trailing commas.
    time_stamps = [t.strip() for t in user_input.split(",") if t.strip()]
    print("Scheduled times:", time_stamps)
    
    for time_stamp in time_stamps:
        thread = threading.Thread(target=Hitting_url, args=(time_stamp,))
        thread.start()