import subprocess

log = subprocess.getoutput("grep 'Failed password' /var/log/auth.log")

if log:
    print("Failed login attempts detected")
else:
    print("No failed login attempts")