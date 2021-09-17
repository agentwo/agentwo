import smtplib
import time
import ssl

print("""
THIS IS A JUST MAIL SENDER, NOT MAIL CLIENT. ONLY FOR LEGAL PURPOSE
""")
context = ssl.create_default_context()
smtp_address = input("Mail server address? ")
while True:
    username = input("Username? ")
    password = input("Password? ")
    try:
        smtp_port = int(input("Mail server port? "))
        break
    except:
        time.sleep(1)
        print("Enter a port NUMBER. ")
        time.sleep(1)
while True:
    ssl = input("Do you want a use SSL or TLS? (Y/N) ")
    if ssl == "N":
        time.sleep(1)
        print("Ok, wait \n")
        time.sleep(1)
        while True:
            try:
                server = smtplib.SMTP(smtp_address, smtp_port)
                server.login(username, password)
                print("Succesed connetted")
            except:
                print("Error, please check server address or port")
                break
        time.sleep(1)
        print("You are now using nothing")
        break
    if ssl == "Y":
        que1 = input("SSL or TLS? ")
        if que1 == "SSL":
            print("Ok, wait \n")
            time.sleep(1)
            while True:
                try:
                    server = smtplib.SMTP_SSL(smtp_address, smtp_port)
                    server.login(username, password)
                    print("You are using now SSL")
                    print("Successed connetted")
                    break
                except smtplib.SMTPAuthenticationError:
                    print("Error, please check username or password.")
                    break
                except OSError:
                    print("Connettion not successfull, please try again later. ")
                    break
            time.sleep(1)
            break
        if que1 == "TLS":
            print("Ok, wait \n")
            time.sleep(1)
            while True:
                try:
                    server = smtplib.SMTP(smtp_address, smtp_port)
                    server.ehlo()
                    server.starttls()
                    server.login(username, password)
                    print("Successed connetted")
                    print("You are now using TLS")
                    break
                except smtplib.SMTPAuthenticationError:
                    print("Error, please check username or password.")
                    break
                except OSError:
                    print("Connettion not successfull, please try again later. ")
                    break
            break
frm = username
to = input("To? ")
message = input("Message? ")
try:
    server.sendmail(frm, to, message)
    print("Successed sended, please check inbox.")
except smtplib.SMTPSenderRefused:
    print("Server refused sending. ")