import smtplib

sender = 'sudheer_ss@yahoo.com'
receivers = ['sudheer_ss@yahoo.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('mail.yahoo.com')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except:
   print "Error: unable to send email"
