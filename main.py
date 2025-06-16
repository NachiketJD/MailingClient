import smtplib
from email import encoders # This is used to encode the attachment
from email.mime.multipart import MIMEMultipart # This is used to create a multipart message
from email.mime.base import MIMEBase # This is used to create a base message
from email.mime.text import MIMEText # This is used to create a text message

server = smtplib.SMTP('smtp.gmail.com', 25) # This line of code, is used to connect to the Gmail server 
server.ehlo() # This line of code, is used to send an email to the Gmail server

with open('password.txt', 'r') as f:
    password = f.read() # This line of code, is used to read the password from the password.txt file the password is encrypted and stored in the password.txt file then, it is read and used to login to the Gmail server.

server.login('mailtest@mail.com', password) # This line of code, is used to login to the Gmail server using the email and password 
