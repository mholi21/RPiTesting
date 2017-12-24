import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = "from@address.com"
toaddr = "to@address.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Subject Title"

body = "Body Text"
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(fromaddr,"password")
text = msg.as_string()
server.sendmail(fromaddr,toaddr,text)
server.quit()