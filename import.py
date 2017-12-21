import os

from Gmail import GetEmailBody
from Gmail import GetService
from Gmail import GetEmailIDs

service = GetService()

def DownloadEmails(email):
    dirname = "download/{}".format(email)
    # if no directory, create it
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    for email_id in GetEmailIDs(service, email):
        body = GetEmailBody(service, email_id)
        CreateEmailTextFile = open("{}/{}.txt".format(dirname, email_id), "wb")
        CreateEmailTextFile.write("\n".join(body))
        print "email downloaded"
    
    print "full download complete"

DownloadEmails("andria.coyne@gmail.com")
