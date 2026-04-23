import psutil

CPU_THRESHOLD = 80

cpu = psutil.cpu_percent(interval=1)

if cpu > CPU_THRESHOLD:
    print(f"High CPU Usage Alert: {cpu}%")
else:
    print(f"CPU usage normal: {cpu}%")

