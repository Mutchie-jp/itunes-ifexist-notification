import smtplib

class sendmail():
    def __init__(self):
        self.smtp_host = "smtp.gmail.com"
        self.smtp_port = 465
        self.username = "s.kinjo0408@gmail.com"
        self.password = "RvDZL2pP8mjB"
        self.from_address = "s.kinjo0408@gmail.com"
        self.to_address = "ricca1539@gmail.com"
        self.subject = "Majo to Hyakkihei no arrange sound track ga saihan saremasita!!!!"
        self.body = "buy now!!"
        self.message = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s" % (self.from_address, self.to_address, self.subject, self.body))

    def sendmail(self):
        smtp = smtplib.SMTP_SSL(self.smtp_host, self.smtp_port)
        smtp.login(self.username, self.password)
        smtp.sendmail(self.from_address, self.to_address, self.message)
        smtp.sendmail(self.from_address, self.to_address, self.message)
        smtp.sendmail(self.from_address, self.to_address, self.message)
