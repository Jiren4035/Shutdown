import os
import platform

def shutdown_windows():
    if platform.system() == "Windows":
        print("Shutting down system in 1 second...")
        os.system("shutdown -s -t 1")
    else:
        print("This script is intended for Windows systems only.")

if __name__ == "__main__":
    shutdown_windows()
