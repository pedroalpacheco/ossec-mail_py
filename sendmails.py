import smtplib
# Specifying the from and to addresses
from email.mime.text import MIMEText



def gomail():
    arqstoragehash = '/var/ossec/logs/alerts/alerts.log'

    #"Send mail"
    fromaddr = 'mail@mail.com'
    toaddrs = 'tomail@tomail.com'

    # Writing the message (this message will appear in the email)

    subject = 'Subject: OSSEC SERVER NAME \n'

    arquivo = open(arqstoragehash, 'rb')
    arquivolido = MIMEText(arquivo.read())
    arquivo.close()

    strarquivo = str(arquivolido)

    msg = subject + strarquivo

    # Gmail Login

    username = 'mail@mail.com'
    password = '**********'

    # Sending the mail

    server = smtplib.SMTP('smtp.mail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

    # print(arquivolido)

#gomail()