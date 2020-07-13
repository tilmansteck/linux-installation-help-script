import os
import time
import platform


# class for console colors (best success on linux based systems)
class color:
    END = '\33[0m'
    BOLD = '\33[1m'
    ITALIC = '\33[3m'
    URL = '\33[4m'
    BLINK = '\33[5m'
    BLINK2 = '\33[6m'
    SELECTED = '\33[7m'

    BLACK = '\33[30m'
    RED = '\33[31m'
    GREEN = '\33[32m'
    YELLOW = '\33[33m'
    BLUE = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE = '\33[36m'
    WHITE = '\33[37m'

    BLACKBG = '\33[40m'
    REDBG = '\33[41m'
    GREENBG = '\33[42m'
    YELLOWBG = '\33[43m'
    BLUEBG = '\33[44m'
    VIOLETBG = '\33[45m'
    BEIGEBG = '\33[46m'
    WHITEBG = '\33[47m'

    GREY = '\33[90m'
    RED2 = '\33[91m'
    GREEN2 = '\33[92m'
    YELLOW2 = '\33[93m'
    BLUE2 = '\33[94m'
    VIOLET2 = '\33[95m'
    BEIGE2 = '\33[96m'
    WHITE2 = '\33[97m'

    GREYBG = '\33[100m'
    REDBG2 = '\33[101m'
    GREENBG2 = '\33[102m'
    YELLOWBG2 = '\33[103m'
    BLUEBG2 = '\33[104m'
    VIOLETBG2 = '\33[105m'
    BEIGEBG2 = '\33[106m'
    WHITEBG2 = '\33[107m'


# script start banner
def banner():
    os.system("clear")

    print(color.YELLOW2 + "  __       __  .__   __.  __    __  ___   ___ ")
    print(color.YELLOW2 + " |  |     |  | |  \ |  | |  |  |  | \  \ /  / ")
    print(color.YELLOW2 + " |  |     |  | |   \|  | |  |  |  |  \  V  /  ")
    print(color.YELLOW2 + " |  |     |  | |  . `  | |  |  |  |   >   <   ")
    print(color.YELLOW2 + " |  `----.|  | |  |\   | |  `--'  |  /  .  \  ")
    print(color.YELLOW2 + " |_______||__| |__| \__|  \______/  /__/ \__\ ")
    print(" ")
    print(color.YELLOW2 + "** Linux installation manager by Tilman Steck **")
    print(" ")


# default installer
def installer():
    print(color.YELLOW2 + "\n[*] Starting installation...\n" + color.GREEN2)

    os.system("apt-get install sudo")

    os.system("sudo apt-get update")
    os.system("sudo apt-get upgrade")

    time.sleep(0.5)


# installer for important programms
def programm_installer():
    nano = input(color.BLUE2 + "\nDo you want to install console text editor 'nano'? y or n: " + color.GREEN2)

    # nano installation
    if nano == "y" or nano == "Y":
        os.system("sudo apt-get install nano")

    else:
        pass

    # python installation
    python = input(color.BLUE2 + "\nDo you want to download 'python'? y or n: " + color.GREEN2)

    if python == "y" or python == "Y":
        os.system("sudo apt-get install python")
        os.system("sudo apt-get install python3")

    else:
        pass

    # git installation
    python = input(color.BLUE2 + "\nDo you want to download 'git'? y or n: " + color.GREEN2)

    if python == "y" or python == "Y":
        os.system("sudo apt-get install git")

    else:
        pass

    # screen installation
    screen = input(color.BLUE2 + "\nDo you want to download 'screen'? y or n: " + color.GREEN2)

    if screen == "y" or screen == "Y":
        os.system("sudo apt-get install screen")

    else:
        pass

    # htop installation
    htop = input(color.BLUE2 + "\nDo you want to download taskmanager 'htop'? y or n: " + color.GREEN2)

    if htop == "y" or htop == "Y":
        os.system("sudo apt-get install htop")

    else:
        pass

    # installation done
    print(color.BLUE2 + "\n\n[*] To complete the installation please write 'done'." + color.GREEN2)
    end = input()

    if end == "done":
        print(color.BLUE2 + "\n[*] Installation is done now!\n" + color.END)
        os._exit(1)

    else:
        exit()


banner()

if platform.system() == "Linux":

    # use installer or not
    i1 = input(color.BLUE2 + "\nDo you want to use the default linux installer? y or n: ")

    if i1 == "y" or i1 == "Y":
        installer()

    else:
        pass

    # install also important programs
    i2 = input(color.BLUE2 + "\nDo you want to install a few important programs? y or n:")

    if i2 == "y" or i2 == "Y":
        programm_installer()

    else:
        pass

    print(color.BLUE2 + "\n[*] Installation is done now! \n" + color.END)
    os._exit(1)

else:
    print(color.RED2 + "\n[*] This installation manager only runs on Linux Based Systems!" + color.END)
    os._exit(1)
