import os
import time

wait_time = 60*10
program = "spotify.exe"
print(f'Waiting: {wait_time} seconds before closing {program}')

for second in range(wait_time, 0, -1):
    os.system('cls')
    print(f'{second // 60:02d}:{second % 60:02d} until \'{program}\' will be terminated.')
    time.sleep(1)

os.system(f'taskkill/im {program}')