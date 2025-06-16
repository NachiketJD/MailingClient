import smtplib

server = smtplib.SMTP('smtp.gmail.com', 25) # This line of code, is used to connect to the Gmail server 
server.ehlo() # This line of code, is used to send an email to the Gmail server

with open('password.txt', 'r') as f:
    password = f.read() # This line of code, is used to read the password from the password.txt file the password is encrypted and stored in the password.txt file then, it is read and used to login to the Gmail server.