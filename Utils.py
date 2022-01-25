import smtplib, traceback
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

class Sender:
    def __init__(self, hostname, port, username, password):
        # self.hostname = hostname
        # self.port = port
        # self.username = username
        # self.password = password
        self.email_server = smtplib.SMTP(hostname, port)
        self.email_server.starttls()
        self.email_server.login(username, password)
    def send_message(self, email):
        try:
            self.email_server.send_message(email)
        except smtplib.SMTPException as se:
            error_message = traceback.format_exc()
            print(error_message)
    def close(self):
        self.email_server.quit()
    @staticmethod
    def checks(*params):
            error_list = []
            if isinstance(params[0], list) and len(params[0]) == 0:
                error_list.append("To can't be an empty list")
            for param in params:
                if type(param) != list:
                    error_list.append(f"'{param}' should be a list")
            if len(error_list):
                raise Exception(",".join(error_list))
    def send_mail(self, From, To, Subject, Message, Cc=[], Bcc=[], Attachments=[]):
        Sender.checks(To, Cc, Bcc)
        email = MIMEMultipart()
        email["From"] = From
        email["To"] = ",".join(To)
        email["Subject"] = Subject
        email.attach(MIMEText(Message, 'plain'))
        email["Cc"] = ",".join(Cc)
        email["Bcc"] = ",".join(Bcc)
        if Attachments:
            for File in Attachments:
                attachment = MIMEApplication(open(File, "rb").read())
                attachment.add_header('Content-Disposition', 'attachment', filename=File)
                email.attach(attachment)
        self.send_message(email)
        self.close()

        
    