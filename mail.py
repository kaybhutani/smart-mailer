import smtplib
from getpass import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
def mailf(ids, msg):
	fromaddr = "jyc128.pr@gmail.com"
	toaddr = ids 
	# instance of MIMEMultipart
	email_body = "Test"
	msg = MIMEMultipart()
	 
	# storing the senders email address  
	msg['From'] = fromaddr
	 
	# storing the receivers email address 
	msg['To'] = toaddr
	 
	# storing the subject 
	msg['Subject'] = "Welcome Fresher"
	 
	# string to store the body of the m

	# attach the body with the msg instance

	#msg.attach(MIMEText(body, 'plain'))

	msg.as_string().encode()
	
	# open the file to be sent 
	filename = "download.jpg"
	with open(filename, "rb") as attachment:
	# instance of MIMEBase and named as p
		p = MIMEBase('application', 'octet-stream')
	# To change the payload into encoded form
		p.set_payload(attachment.read())
	# encode into base64
		encoders.encode_base64(p)
	  
	p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
	 
	# attach the instance 'p' to instance 'msg'
	msg.attach(p)
	 
	# creates SMTP session
	s = smtplib.SMTP('smtp.gmail.com', 587)
	 
	# start TLS for security
	s.starttls()
	password="Enter the password"
	# Authentication
	s.login(fromaddr,password)
	 
	# Converts the Multipart msg into a string
	text = msg.as_string()
	 
	# sending the mail
	s.sendmail(fromaddr, toaddr, text)
	 
	# terminating the session
	s.quit()

msg="Welcome to JIIT, CONNECT WITH US AT: \n www.jiitconverge.in \n www.facebook.com/jiitconverge \n www.instagram.com/jiitconverge \n www.snapchat.com/add/jiitconverge20  \nFor more, Contact \n Siddharth: +91 8512032088"
data=pd.read_excel("data.xlsx")


for i in range(len(data)):
	mailf(data["Email"][i],msg)
	print("Email sent")
