import pywhatkit

print("Please open whatsapp web in your browser to automate your message")
print("Enter the reciever mobile number")
n = input()
print("Enter the message to be forwarded")
m = input()
print("Enter time (hr-min), newline wise")
hr = int(input())
mi = int(input())



pywhatkit.sendwhatmsg(n,m,hr,mi)
print("Message has been forwarded to",n)

