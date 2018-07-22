import smtplib
from getpass import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
def mailf(name, ids):
	fromaddr = "kbhutani0001@gmail.com"
	toaddr = ids 
	# instance of MIMEMultipart
	msg = MIMEMultipart()
	 
	# storing the senders email address  
	msg['From'] = fromaddr
	 
	# storing the receivers email address 
	msg['To'] = toaddr
	 
	# storing the subject 
	msg['Subject'] = "{} Welcome To Prismatic Family!".format(name)
	 
	# string to store the body of the m
	body = "Thankyou for registering in Prismatic. We have added everyone to our Whatsapp group, In case you have not been added,  join by clicking this link: https://chat.whatsapp.com/17v9pdqAL6YCIVAjh78zdG.\nFollow our Facebook page for more details - https://www.facebook.com/prismatic128/  \nFor more, Contact \n Shivang garg: +91 88821 19197\n Kartikay Bhutani: +91 8802999631"
	 
	# attach the body with the msg instance
	msg.attach(MIMEText(body, 'plain'))
	 
	# open the file to be sent 
	filename = "welcome.jpg"
	attachment = open("welcome.jpg", "rb")
	 
	# instance of MIMEBase and named as p
	p = MIMEBase('application', 'octet-stream')
	 
	# To change the payload into encoded form
	p.set_payload((attachment).read())
	 
	# encode into base64
	encoders.encode_base64(p)
	  
	p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
	 
	# attach the instance 'p' to instance 'msg'
	msg.attach(p)
	 
	# creates SMTP session
	s = smtplib.SMTP('smtp.gmail.com', 587)
	 
	# start TLS for security
	s.starttls()
	password="kayb0001"
	# Authentication
	s.login(fromaddr,password)
	 
	# Converts the Multipart msg into a string
	text = msg.as_string()
	 
	# sending the mail
	s.sendmail(fromaddr, toaddr, text)
	 
	# terminating the session
	s.quit()

data=pd.read_excel("data.xlsx")

for i in range(len(data)):
	mailf(data["Name"][i], data["Email"][i])
