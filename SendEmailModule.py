from email.message import EmailMessage
import smtplib

def SendEmail(fileName,sender,reciver):
    try:
        app_password = "lfsh kyyl vywc ffjn"

        msg = EmailMessage()

        msg['subject'] = 'Log File report'
        msg['From'] = sender
        msg['To'] = reciver
        msg.set_content("Please find the attached log file")

        msg.add_attachment(open(fileName,'rb').read(),maintype='automation application',subtype='octet-stream',filename=fileName)

        smtp = smtplib.SMTP_SSL('smtp.gmail.com',465)
        smtp.login(sender,app_password)
        smtp.send_message(msg)
        smtp.quit()

        print("Email Send")
    
    except Exception:
        print("Exception occured while sending email notification")