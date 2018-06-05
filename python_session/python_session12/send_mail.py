import smtplib
#from email.MIMEMultipart import MIMEMultipart
#from email.MIMEText import MIMEText

fromaddr = "sudheer_ss@yahoo.com"
toaddr = "sudheer_sss@yahoo.com"

text = "text message sent from python"

username = "sudheer_ss@yahoo.com"
password = "Python@123"

#msg = MIMEMultipart()
"""
msg['From'] = fromaddr
msg['To'] = toaddr

msg['Subject'] = "Test"

msg.attach(MIMEText(text))
"""
server = smtplib.SMTP('smtp.mail.yahoo.com:587')
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
#server.sendmail(fromaddr, toaddr, msg.as_string())
server.sendmail(fromaddr, toaddr, "hi there")
server.quit()

