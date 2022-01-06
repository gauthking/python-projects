import pywhatkit
import time
import pyautogui
import keyboard as k

def sendmsg(n,m,hr,mi):
    pywhatkit.sendwhatmsg(n,m,hr,mi,24)
    pyautogui.click(1050, 950)
    time.sleep(2)
    k.press_and_release('enter')
    print("Message has been forwarded to",n)

print("Please open whatsapp web in your browser to automate your message")
print("Enter the reciever mobile number")
n1 = input()
print("Enter the message to be forwarded")
m1 = input()
print("Enter time (hr-min), newline wise")
hr1 = int(input())
mi1 = int(input())
sendmsg(n1,m1,hr1,mi1)
