import os
import shutil
import datetime
import smtplib
from datetime import datetime

"""Script To Move Files
"""

def FileTransfer() -> tuple:
    """Transfers the FC backup to the cloud drive"""

    DateTimeObj = datetime.now()
    TodayDateStr = DateTimeObj.strftime("%y%m%d")

    BaseOfStr = r"\backup."
    EndOfStr = r"-19"
    FileStr = BaseOfStr + TodayDateStr + EndOfStr
    FileStrForEmail = BaseOfStr + TodayDateStr + EndOfStr

    SourcePath = r"F:\FC_Backups" + FileStr

    DestinationPath =  r"X:\FC_BACKUPS"

    shutil.copy2(SourcePath, DestinationPath)
    return FileStrForEmail, SourcePath, DestinationPath

def CompletetionEmailNotification(EmailStrAndBothPaths:tuple) -> None:
    """Sends email if the file transfer is successful"""

    SERVER = "smtp.example.com"
    FROM = "example@domain.com"
    TO = ["example@domain.com"]
    SUBJECT = "File Transfer Complete"
    TEXT = ("The FC Backup: " + EmailStrAndBothPaths[0] + " was successfully backed up\n\nFrom: " + EmailStrAndBothPaths[1] + "\n\nTo: " + EmailStrAndBothPaths[2])
    message = """From: {0:}\r\nTo: {1:}\r\nSubject: {2:}\r\n\n\n{3:s}""".format(FROM, ", ".join(TO), SUBJECT, TEXT)

    server = smtplib.SMTP(SERVER, 587)
    server.connect(SERVER, 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(FROM, "password")
    server.sendmail(FROM, TO, message)
    server.quit()

def FailureEmailNotification() -> None:
    """Sends email if file trasnfer failed"""

    SERVER = "smtp.example.com"
    FROM = "example@domain.com"
    TO = ["example@domain.com"]
    SUBJECT = "File Transfer Failed!!!"
    TEXT = ("The FC back up Failed, Please go check on it!!")

    message = """From: {0:}\r\nTo: {1:}\r\nSubject: {2:}\r\n\n\n{3:}""".format(FROM, ", ".join(TO), SUBJECT, TEXT)

    server = smtplib.SMTP(SERVER, 587)
    server.connect(SERVER, 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(FROM, "password")
    server.sendmail(FROM, TO, message)
    server.quit()

try:
    CompletetionEmailNotification(FileTransfer())
    print("File Transfer successful")
except:
    FailureEmailNotification()
    print("File Transfer unsuccessful")

