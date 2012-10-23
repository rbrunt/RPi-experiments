###################################################################################
# To make this run at startup, add "/path/to/script/sendIP.py &" to /etc/rc.local #
#       Make sure that you change your email address and SMTP details below!      #
###################################################################################
import subprocess
import smtplib

# Get the output of `ifconfig` and store it in a variable:
ipinfo = subprocess.check_output("ifconfig", shell=True)

# Setup the Message details:
fromaddr = 'notifications@example.com'
# For multiple addresses, add more to the list. For one address, a string will suffice.
toaddrs  = ['john.smith@example.com']

msg = """From: RaspberryPi <notifications@blue-shift.net>
To: John Smith <john.smith@example.com>
Subject: RPi IP information

Here's a print of ifconfig for the RaspberryPi:

""" + ipinfo

# Credentials for your SMTP server:
username = 'username'
password = 'password'

# Acutally sending the mail:
############################
# This defaults to using google's smtp, change it to yours if it's different
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
