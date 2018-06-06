import RPi.GPIO as GPIO
import time
from time import sleep
from datetime import datetime
from decimal import *
from picamera import PiCamera
from smtplib import SMTP
from smtplib import SMTPException
import os
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import os,subprocess
import data_test
import sqlite3
import time
import sys
import csv
# connecting to the database 
connection = sqlite3.connect("myTable.db")
crsr1=connection.cursor()
crsr = connection.cursor()
pht= 27
pht1= 22

camera = PiCamera()
global lmn,dt,dt1,diff,deltat
def setup():
     GPIO.setwarnings(False)
     GPIO.setmode(GPIO.BCM)
     GPIO.setup(pht, GPIO.IN)
     GPIO.setup(pht1,GPIO.IN)
     GPIO.setup(2,GPIO.OUT)
     GPIO.output(2,GPIO.LOW)
     global i
     i=0
def loop():
        j=0
        print('System ON')
        while (True):
            x= GPIO.input(pht)
            y= GPIO.input(pht1)
            if(x==GPIO.HIGH and y==GPIO.LOW):
               camera.rotation= 180
               camera.start_preview(alpha=155)
               GPIO.output(2,GPIO.LOW)
               dt=datetime.now()
               print('sensor 1 Triggered at:',dt)
               print('Car entered')
               y=GPIO.input(pht1)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
               if(y==GPIO.LOW):
                   while(y==GPIO.LOW):
                    
                    y=GPIO.input(pht1)
                    
                    if(y==GPIO.HIGH):
                        exit
                        
                       
               dt1=datetime.now()
               print('sensor 2 triggered at:',dt1)
               diff=dt1-dt
               print('Time diff', diff)
               dist= 0.05
               deltat = diff.seconds + (diff.microseconds/1000000)
               print('Deltat Time :', deltat)
               D= dt.day
               M=dt.month
               Y=dt.year
               H=dt.hour
               sec=dt.second
               Min=dt.minute
               getcontext().prec = 2 
               vel=dist/deltat
               print('Speed:',vel)
               j=j+1
               print(j)
               if(vel>0.05):
                    print('Overspeeding')
                    GPIO.output(2,GPIO.HIGH)
                    global i
                    i=i+1
                    
                    time.sleep(0.5)
                    GPIO.output(2,GPIO.LOW)
                    camera.capture('/home/pi/Desktop/image%i.png' %i)
                    cwd = os.getcwd()
                    subprocess.call(["mv",os.path.join(cwd,"Desktop","processed_imgs",'image1.jpg'),os.path.join('/home/pi/Desktop','image1.jpg')])
                    msg=MIMEMultipart()
                    msg['subject']='Overspeed Detected'
                    sender='lntlntlnt390019@gmail.com'
                    msg['From']=sender
                    time.sleep(2)
                    
                    def_file=open("/home/pi/Desktop/def_list.txt","r+",1)
                    lines=def_file.readlines()
                    
                    file=('/home/pi/Desktop/processed_imgs/image1.jpg')
                    attachment=open(file,'rb')
                    img=MIMEImage(attachment.read())
                    msg.attach(img)
                    body =MIMEText(("Speed=%f \n Date & time of occurence:%i-%i-%i  %i:%i:%i ") %(vel,D ,M, Y, H, Min, sec))
                    msg.attach(body)
                    mail=smtplib.SMTP('smtp.gmail.com',587)
                    mail.ehlo()
                    mail.starttls()
                    mail.login('lntlntlnt390019@gmail.com','Lnt12345678@')
                    for line in lines:
                        k=line.rstrip('\n')
   
                        t=(k,)
                        print(k)
                        crsr1.execute('SELECT mail FROM emp WHERE license =?',t )
                        ans=crsr1.fetchone()
                        if ans is not None:
                             lmn=ans[0]
                        #for rx in ans:
                        else:
                             lmn='abhilashdecember@gmail.com'
                        print(lmn)
                        msg['To'] = lmn
                        text= msg.as_string()
                        def_file=open("/home/pi/Desktop/def_list.txt","r+",1)
                        def_file.truncate()
                    
                        mail.sendmail('lntlntlnt390019@gmail.com',lmn,text)
                    crsr.close()
                    mail.close()
                    crsr1.close()
                    connection.close()

               else:
                        print('All clear')
                        dt1=0
                        dt=0
               
               #GPIO.output(2,GPIO.LOW)
               #time.sleep(1.0)
            elif (y==GPIO.HIGH and x==GPIO.HIGH):
                dt1=0
                dt=0
                print('make way clear')
def endprogram():
    GPIO.cleanup()
    camera.stop_preview()
if __name__ == '__main__':
    setup()
    try:
        
        loop()
    except KeyboardInterrupt:
        
        endprogram()
