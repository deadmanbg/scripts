from datetime import datetime
import urllib.request
import time
import socket

on = True
start_time = start_time_str = None
while True:
    try:
        time.sleep(1)
        s = socket.socket()
        s.settimeout(1)
        s.connect(('8.8.8.8', 53))
        if on == False:
            end_time = datetime.now()
            end_time_str = end_time.strftime("%d.%m.%Y %H:%M:%S")
            print('Online  ' + end_time_str)
            with open('offline.txt', 'a') as f:
                total = end_time - start_time
                if total.total_seconds() > 2:
                    f.write(start_time_str + ' - ' + end_time_str + ': total ' + str(total) + '\n')
        s.close()
        on = True
    except Exception:
        if on:
            on = False
            start_time = datetime.now()
            start_time_str = start_time.strftime("%d.%m.%Y %H:%M:%S")
            print('Offline ' + start_time_str)
