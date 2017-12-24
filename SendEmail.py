import RPi.GPIO as GPIO
import smtplib
import time
from time import sleep
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

GPIO.setmode(GPIO.BCM)

#DO NOT USE PIN2 OR PIN3 HARD-WIRED PULL_UP
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

fromaddr = "from@address.com"
toaddr = "to@address.com"

try:
	while True:
		if(GPIO.input(4)):
			msg = None
			readable=time.ctime(time.time())
			body = "Something happened on: " + readable
			msg = MIMEMultipart()
			msg['From'] = fromaddr
			msg['To'] = toaddr
			msg['Subject'] = "RPi Report!"
			msg.attach(MIMEText(body, 'plain'))
			server = smtplib.SMTP('smtp.gmail.com',587)
			server.starttls()
			server.login(fromaddr,"password")
			text = msg.as_string()
			server.sendmail(fromaddr,toaddr,text)
			server.quit()
			#PAUSE TO ONLY SEND ONCE EVERY X SECONDS
			sleep(5)
#RUNNING UNTIL IT'S CANCLED BY KEYBOARD INPUT (CTRL+C)
except KeyboardInterrupt:
	GPIO.cleanup()