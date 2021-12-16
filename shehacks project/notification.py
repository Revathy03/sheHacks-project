import datetime                                                    # medicine notifier
from plyer import notification
from array import *
choice="y"
name=[]                                                              #declarations
notiH=  []
notiM= []
interH= []
interM= []
a=[]
b=[]
count=0
while(choice=="y"):
  name.append(str(input("Please type the name of medicine:  "))) 
  print("Enter time details in 24hr format :")                         #details of time for first consumption of medicine
  notiH.append(int(input("What hour do you want to be notified:  ")))
  notiM.append(int(input("What minute do you want to be notified:  ")))
  print("Time interval after which next intake to be scheduled ")
  interH.append(int(input("Time interval in hrs: ")))                  #time break for the next consumption of medicine
  interM.append(int(input("Time interval in mins: ")))
  a.append(notiH)
  b.append(notiM)
  choice=str(input("Do you want to enter next medicine (y/n): "))      #input more medicines?
  count=count+1
print("You will be notified at ",notiH[0],notiM[0])
print("for medicine ",name[0])
while(1==1):
    for i in range(count):
        if(notiH[i]==datetime.datetime.now().hour and notiM[i]==datetime.datetime.now().minute): #check if it is time for the medicine
            title=name[i]
            message='PLEASE TAKE YOUR MEDICINE! '
            notification.notify(title=title, message=message, app_icon="Graphicloads-Medical-Health-Medicine-box-2.ico", timeout=10, toast=False )
            notiH[i]=notiH[i]+interH[i]
            notiM[i]=notiM[i]+interM[i]
            if(notiM[i]>=60):                       #check if it is an end of a hour
                notiM[i]=notiM[i]%60
                notiH[i]=notiH[i]+1
            if(notiH[i]>=24):                       #check if next day begins
                notiH[i]=a[i]                       #set time details to the time for first consumption of the day
                notiM[i]=b[i]
            print("You will be notified at ",notiH[i],notiM[i])
            print("for medicine ",name[i])


       