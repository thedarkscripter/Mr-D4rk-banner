import os
import time

def premium_banner():
    os.system("clear")  # Clear the terminal screen
    print("\033[1;32m" + "=" * 50)  # Green color text for top border
    print("\033[1;31m" + "   ███╗   ███╗██████╗      ██████╗ ██████╗ ██╗  ██╗")
    print("\033[1;31m" + "   ████╗ ████║██╔══██╗    ██╔════╝██╔═══██╗██║ ██╔╝")
    print("\033[1;32m" + "   ██╔████╔██║██████╔╝    ██║     ██║   ██║█████╔╝ ")
    print("\033[1;32m" + "   ██║╚██╔╝██║██╔═══╝     ██║     ██║   ██║██╔═██╗ ")
    print("\033[1;31m" + "   ██║ ╚═╝ ██║██║         ╚██████╗╚██████╔╝██║  ██╗")
    print("\033[1;31m" + "   ╚═╝     ╚═╝╚═╝          ╚═════╝ ╚═════╝ ╚═╝  ╚═╝")
    print("\033[1;32m" + "=" * 50)  # Green color text for bottom border
    print("\033[1;36m" + "           Banner Name: MR D4RK")
    print("\033[1;36m" + "           Developer: MD SOFIKUL ISLAM ")
    print("\033[1;36m" + "           GitHub: github.com/MR_D4RK")
    print("\033[1;36m" + "           Version: 1.0")
    print("\033[1;32m" + "=" * 50)

# Run the banner
premium_banner()