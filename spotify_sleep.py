import os
import time

PROCESS_NAME = "spotify.exe"
DEFAULT_LENGTH = 10  # default length of sleep timer in minutes
COUNTDOWN_INTERVAL = 1 # length of a single countdown interval in seconds

print("Just hit enter for default 10 minutes ->")

while True:
    try:
        minutes = input("Sleep timer duration (minutes) : ") 
        minutes = minutes if minutes else DEFAULT_LENGTH
        
        total_seconds = 60*int(minutes)  # user input for sleep timer length
        break  
    except ValueError:
        print('\nERROR: Please enter a valid integer value for the duration in minutes.')

for second in range(total_seconds, 0, -COUNTDOWN_INTERVAL):
    print(f'{second // 60:02d}:{second % 60:02d} until \'{PROCESS_NAME}\' will be terminated.')  # print the remaining time
    time.sleep(COUNTDOWN_INTERVAL)  # wait for countdown interval
    os.system('cls')  # clear console

# NOTE: not using the force option (/f) here allows spotify to keep the user's timestamp in the song
os.system(f'taskkill/im {PROCESS_NAME}')  # kill program and all child processes 