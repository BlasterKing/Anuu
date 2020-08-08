import urllib,requests
import time,sys
print('''\033[1;33m ____  __  __ ____
/ ___||  \/  / ___|  _ __  _   _
\___ \| |\/| \___ \ | '_ \| | | |
 ___) | |  | |___) || |_) | |_| |
|____/|_|  |_|____(_) .__/ \__, |
                    |_|    |___/
   ->[ANUPA DINURANGA]<-''')
print("\033[1;31m<<<_____________________________>>>\n")
while True:
    num=int(input("\033[1;36mNumber:"))
    msg=input("Message:")
    url="https://sv2.ideamarthosting.dialog.lk/lakpriya1016Apps/wapp/otp2.php"
    body={"id":num,"apphash":msg}

    print("\033[1;31m<------waiting------>")
    r=requests.post(url,json=body)
    print("\033[1;32m[ ..Successfully sent.. ]")
    c=input("\033[1;90mDo you want send message again? -")
    if c.lower()=="y":
        continue 
    else:
        print("\033[1;37m_GOOD BYE_")
        break