import psutil

DISK_THRESHOLD = 20

disk = psutil.disk_usage('/')
free_percent = disk.free / disk.total * 100

if free_percent < DISK_THRESHOLD:
    print("Low Disk Space Alert")
else:
    print("Disk usage normal")