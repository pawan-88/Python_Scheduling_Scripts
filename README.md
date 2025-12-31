# API Scheduler

This script to hit ifconfig.co at specific times. Uses threads if you have duplicate timestamps.

## Run it
- python main.py

Then just add timestamps into this below format-
- Enter the timestamps (comma separated, HH:MM:SS): 09:15:00,13:45:00

## Files
- main.py - main file.
- scheduler.py - scheduler login and api call.
- test_scheduler.py - write test cases for scheduler.py its code run correct or not.
- Log.txt - create file when scheduler run

## How it works
Formatting_Time - this function helps for format the timestamps into real time.
Hitting_Url - this function helps to call the api and print actual statements.
main - this used for call main file.

## used Python 3.13 or whatever version you got