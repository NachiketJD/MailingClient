import smtplib

server = smtplib.SMTP('smtp.gmail.com', 25) # This line of code, is used to connect to the Gmail server 
server.ehlo() # This line of code, is used to send an email to the Gmail server