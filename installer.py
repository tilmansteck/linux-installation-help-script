import os
import time


# script start banner
def banner():
    text = f"""
  __       __  .__   __.  __    __  ___   ___ 
 |  |     |  | |  \ |  | |  |  |  | \  \ /  / 
 |  |     |  | |   \|  | |  |  |  |  \  V  /  
 |  |     |  | |  . `  | |  |  |  |   >   <   
 |  `----.|  | |  |\   | |  `--'  |  /  .  \  
 |_______||__| |__| \__|  \______/  /__/ \__\ 
                                            
** Linux installation manager by Tilman Steck **

NOTE: [*] Installation is starting!\n\n\n
    """

    time.sleep(1)
    print(text)


# default installer
def installer():
    print("[*] Starting installation...\n\n")

    os.system("apt-get install sudo")

    os.system("sudo apt-get update")
    os.system("sudo apt-get upgrade")

    time.sleep(1)


# installer for important programms
def programm_installer():
    nano = input("Do you want to install console text editor 'nano'? y or n: ")

    # nano installation
    if nano == "y" or nano == "Y":
        os.system("sudo apt-get install nano")

    else:
        pass

    # python installation
    python = input("Do you want to download 'python'? y or n: ")

    if python == "y" or python == "Y":
        os.system("sudo apt-get install python")

    else:
        pass

    # screen installation
    screen = input("Do you want to download 'screen'? y or n: ")

    if screen == "y" or screen == "Y":
        os.system("sudo apt-get install screen")

    else:
        pass

    # htop installation
    htop = input("Do you want to download taskmanager 'htop'? y or n: ")

    if htop == "y" or htop == "Y":
        os.system("sudo apt-get install htop")

    else:
        pass

    # installation done
    print("\n\n[*] To complete the installation please write 'done'.")
    end = input()

    if end == "done":
        exit()

    else:
        exit()


banner()

# use installer or not
i1 = input("Do you want to use the default linux installer? y or n: ")

if i1 == "y" or i1 == "Y":
    installer()

else:
    exit()

# install also important programs
i2 = input("Do you want to install a few important programs? y or n:")

if i1 == "y" or i1 == "Y":
    programm_installer()

else:
    exit()

print("[*] Installation is done now!")
exit()
