import smtplib
import config
import time
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
            #Where my send email logic goes
            try:
                server = smtplib.SMTP('smtp.gmail.com:587')
                server.ehlo()
                server.starttls()
                try:
                    server.login(config.MY_ADDRESS, config.PASSWORD) 
                except:#Attempt 1 wait 20 mins
                    server.login(config.MY_SECOND_ADDRESS, config.SECOND_PASSWORD)

                    message = "Waiting attempt # 1."
                    server.sendmail(config.MY_SECOND_ADDRESS, "8324506550@txt.att.net", message) #frm, to, msg
                    server.quit()

                    print("Waiting attempt # ", waitCount)
                    waitCount = waitCount + 1
                    mins = 0
                    while mins != 20:
                        # Sleep for a minute
                        time.sleep(60)
                        # Increment the minute total
                        mins += 1
                    x=x-1
                    
                    try:
                        server.login(config.MY_ADDRESS, config.PASSWORD)
                    except:#Attempt 2 wait 20 mins
                        server.login(config.MY_SECOND_ADDRESS, config.SECOND_PASSWORD)

                        message = "Waiting attempt # 2."
                        server.sendmail(config.MY_SECOND_ADDRESS, "8324506550@txt.att.net", message) #frm, to, msg
                        server.quit()
                        
                        print("Waiting attempt # ", waitCount)
                        waitCount = waitCount + 1
                        mins = 0
                        while mins != 20:
                            # Sleep for a minute
                            time.sleep(60)
                            # Increment the minute total
                            mins += 1

                        try:
                            server.login(config.MY_ADDRESS, config.PASSWORD)
                        except:#Attempt 3 wait 20 mins
                            server.login(config.MY_SECOND_ADDRESS, config.SECOND_PASSWORD)

                            message = "Waiting attempt # 3."
                            server.sendmail(config.MY_SECOND_ADDRESS, "8324506550@txt.att.net", message) #frm, to, msg
                            server.quit()

                            print("Waiting attempt # ", waitCount)
                            waitCount = waitCount + 1
                            mins = 0
                            while mins != 20:
                                # Sleep for a minute
                                time.sleep(60)
                                # Increment the minute total
                                mins += 1

                            try:
                                server.login(config.MY_ADDRESS, config.PASSWORD)
                            except:#Final Attempt 
                                server.login(config.MY_SECOND_ADDRESS, config.SECOND_PASSWORD)

                                message = "Waiting till tomorrow..."
                                server.sendmail(config.MY_SECOND_ADDRESS, "8324506550@txt.att.net", message) #frm, to, msg
                                server.quit()

                                print("Waiting till tomorrow...")
                                mins = 0
                                while mins != 1440:
                                    # Sleep for a minute
                                    time.sleep(60)                             
                                    # Increment the minute total
                                    mins += 1   

                message = 'Subject: {}\n\n{}'.format(subject, msg)
                server.sendmail(config.MY_ADDRESS, TO_ADDRESS, message) #frm, to, msg
                server.quit()
                print("Success: Email sent! -> ", x, ".) ", TO_ADDRESS)
                s = open("sentEmails.txt", "a")
                s.write(TO_ADDRESS)
            except:
                print("Email failed to send. -> ", x, ".) ", TO_ADDRESS)



subject = "Gaming Live Stream!"
msg = "Hi There! My name is Shane and I have just started AnotherTechChannel on Youtube. We keep tech simple. We teach coding, web development and even game streaming; among other things like building and repairing computers. Please come check us out and if you like what you see please consider subscribing and clicking the bell icon so you can be notified when we go live! \n\nThank you for your time and support and remember, sharing is caring. \n\nHere's The Link: https://www.youtube.com/channel/UCeSk0tqmNVPfIg1arx2GSOQ/videos?view_as=subscriber \n\n Follow me on Twitter www.twitter.com/@TechTard88"

send_email(subject, msg)