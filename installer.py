import os
import time


def installer():
    print("[*] Starting installation...")

    os.system("apt-get update")
    os.system("apt-get upgrade")

    os.system("apt-get install sudo")
    os.system("apt-get install nano")
    os.system("apt-get install python")

    time.sleep(1)

    print("[*] Installation done!")

    
    
