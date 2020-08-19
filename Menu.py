import os
choice="yes"
while(choice!="no"):
    print("Welcome to Software Automation")
    print("Press 1 for Browser(only Chrome engine is available)\nPress 2 for Media Player(VLC and Windows Media Player)\nPress 3 for Document Editor")
    item=int(input("Enter the option:"))
    if(item==1):
        n=input("Enter the command to open browser:")
        if(("execute" or "open" in n) and("Chrome" in n)):
            os.system("chrome")
    elif(item==2):
        n=input("Enter the command to open media:")
        if(("Play" or "Stream" in n)):
            if("vlc" in n):
                os.system("vlc")
            elif("wmplayer" in n):
                os.system("wmplayer")
    elif(item==3):
        n=input("Enter the command to open editor:")
        if("notepad" in n):
            os.system("notepad")
    choice=input("Would you Like to open another Software:")
print("Thanks for Using menu software")

