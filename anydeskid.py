import shutil
import time
import os

windows_user = os.getenv("username")

os.system("@title AnyDesk ID changer made by Sipo#4285")

print("If you encounter any issues with this, please report them on Cheating Community's discord server!")
print("Initializing in 3 seconds...")
time.sleep(3)
os.system("cls")

print("Resetting ID...")

try:
    shutil.rmtree(r"C:\\Users\\" + windows_user + r"\\AppData\\Roaming\\AnyDesk")
    input("Success, press any enter to exit...")
except:
    input("Failed, press any enter to exit...")
