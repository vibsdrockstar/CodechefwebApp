import webbrowser
import time
import os

profile = input("Enter codechef  profile:")
refresh = input("Enter refresh time in seconds:")
browser = input("Enter your browser (e.g chrome/firefox")
count= input("How many views you want?")

def openURL():
    os.system("TASKILL /F /IM"+browser+".exe")
    webbrowser.open(profile)
    time.sleep(int(refresh))

    for i in range(int(count)):
        print("Profile has been viewed")
        openURL()


openURL()
    
