import psutil

memory = psutil.virtual_memory()

if memory.percent > 80:
    print("High Memory Usage Alert")
else:
    print("Memory usage normal")