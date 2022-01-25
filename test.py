from Utils import Sender
from smtp_config import smtp_server, smtp_port, smtp_user, smtp_pwd
from datetime import datetime

From = "vikram.the.coder@outlook.com"
To = ["vikram@sequoiaat.com", ]
Cc = ["markiv.84@gmail.com", "vikram.the.coder@gmail.com", "vikram.the.coder@outlook.com"]
Bcc = ["markiv.1984@gmail.com",]
Subject = "Test mail"
Msg = f"Testing message: {datetime.now()}"
Attachements = ["sample.txt", "sample2.txt"]

sender = Sender(smtp_server, smtp_port, smtp_user, smtp_pwd)

choice = int(input("Enter Case:"))
print(f"Case {choice}:", end=" ")
if choice == 1:
    print("Mail with mandatory fileds alone")
    sender.send_mail(From, To, Subject, Msg) 
elif choice == 2:
    print("Mail with cc")
    sender.send_mail(From, To, Subject, Msg, Cc=Cc) 
elif choice == 3:
    print("Mail with bcc")
    sender.send_mail(From, To, Subject, Msg, Bcc=Bcc)
elif choice == 4:
    print("Mail with attachments")
    sender.send_mail(From, To, Subject, Msg, Attachments=Attachements)
elif choice == 5:
    print("Mail with cc and bcc")
    sender.send_mail(From, To, Subject, Msg, Bcc=Bcc, Cc=Cc)
elif choice == 6:
    print("Mail with cc and Attachments")
    sender.send_mail(From, To, Subject, Msg, Cc=Cc, Attachments=Attachements)
elif choice == 7:
    print("Mail with bcc and Attachments")
    sender.send_mail(From, To, Subject, Msg, Bcc=Bcc, Attachments=Attachements)
elif choice == 8:
    print("Mail with all options")
    sender.send_mail(From, To, Subject, Msg, Cc=Cc, Bcc=Bcc, Attachments=Attachements)
