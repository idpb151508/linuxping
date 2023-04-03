import subprocess
from time import sleep

def ping():
    try:
        subprocess.check_output(["ping", "-c", "1", "192.168.18.19"])
        return True
    except subprocess.CalledProcessError:
        return False

while True:
    print(ping())
    sleep(3)