import time
timer = 3
time_end = time.time() + timer
while time.time() < time_end:
    print(timer + (time.time() - time_end))
