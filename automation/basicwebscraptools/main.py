import pywhatkit
import wikipedia
import time
import pyautogui
import keyboard as k
# NOTEE:: In the sendmsg function, make sure you set the pyautogui position mouse keys in the whatsapp web text box... THE PREVIOUSLY SET VALUES WORKS ON MOST CASES.. but incase ..
# called functions
def ytplay(link):
    try:
        pywhatkit.playonyt(link)
        print("Playing Now...")
    except:
        print("Network Error Occured... Please Make sure you are connected to the internet..")
def sendmsgc(n,m,hr,mi):
    try:
        pywhatkit.sendwhatmsg(n,m,hr,mi,24)
        pyautogui.click(1535, 985)
        time.sleep(2)
        pyautogui.press('enter')
        print("Message has been forwarded to",n)
    except:
        print("Network Error Occured... Please Make sure you are connected to the internet..")

def googlesearch(search):
    try:
        pywhatkit.search(search)
        print("Searching on google...")
    except:
        print("Network Error Occured... Please Make sure you are connected to the internet..")

def searchinfo(info1,lineno):
    try:
        k = wikipedia.summary(info1, sentences = lineno)
        print("Fetching info..")
        print("There you go..")
        print(k)
    except:
        print("Network Error Occured... Please Make sure you are connected to the internet..")

def main():
    print("Hello There... Welcome to PywhatKIT!")
    print('')
    print("Funcions Available \n 1. Send a WhatsApp Message \n 2. Perform a YouTube Serach \n 3. Perform a Google Search \n 4. Get info about a topic")
    print('')
    print('Please Enter which function you would like to perform(1/2/3/4):')
    func = int(input())
    if func == 1 :
        print("Enter the reciever mobile number(with country code)")
        n1 = input()
        print("Enter the message to be forwarded")
        m1 = input()
        print("Enter time (hr-min), newline wise")
        hr1 = int(input())
        mi1 = int(input())
        sendmsgc(n1,m1,hr1,mi1)      
                


    elif func == 2 :
        print("Enter the URL/Title of the video to play on YouTube:")
        play = input()
        ytplay(play)

    elif func == 3 :
        print("Enter what to search on Google")
        gsearch = input()
        googlesearch(gsearch)

    elif func == 4 :
        print("Enter what info to fetch from the INTERNET:")
        inf = input()
        print("Length of the fetched info:")
        line = int(input())
        searchinfo(inf,line)

main()