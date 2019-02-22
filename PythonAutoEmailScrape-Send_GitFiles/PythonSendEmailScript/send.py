import smtplib
import config
import random

def send_email(subject, msg):
    waitCount = 1

    with open("emails.txt", "r") as lines:
        emails = []
        x=0
        for line in lines:
            emails.append(line)

        while True:
            TO_ADDRESS = random.choice(emails)
            TO_ADDRESS = TO_ADDRESS.strip('\n')
            #Where my send email logic goes
            try:
                server = smtplib.SMTP('smtp.gmail.com:587')
                server.ehlo()
                server.starttls()
                try:
                    server.login(config.MY_ADDRESS, config.PASSWORD) 
                except:#Attempt 1 wait 20 mins
                   Print ("Failed to login. Check Config file.")

                message = 'Subject: {}\n\n{}'.format(subject, msg)
                server.sendmail(config.MY_ADDRESS, TO_ADDRESS, message) #frm, to, msg
                server.quit()
                print("Success: Email sent! -> ", x, ".) ", TO_ADDRESS)
                s = open("sentEmails.txt", "a")
                logSent = TO_ADDRESS + "\n"
                s.write(logSent)
            except:
                print("Email failed to send. -> ", x, ".) ", TO_ADDRESS)
                b = open("failedEmails.txt", "a")
                logBad = TO_ADDRESS + "\n"
                b.write(logBad)



subject = "Write your subject here!"
msg = "Write your message here!!! \n\n Follow me on Twitter www.twitter.com/@TechTard88"

send_email(subject, msg)
