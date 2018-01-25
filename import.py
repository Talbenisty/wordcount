import os
import pdb


from Gmail import GetEmailBody
from Gmail import GetService
from Gmail import GetEmailIDs

service = GetService()


def DownloadEmail(service, email_id, dirname):
    body = GetEmailBody(service, email_id)
    if body != "":
        CreateEmailTextFile = open("{}/{}.txt".format(dirname, email_id), "wb")

        pdb.set_trace()

        CreateEmailTextFile.write("\n".join(body))
    print "email downloaded"


def DownloadEmails(email):
    dirname = "download/{}".format(email)
    # if no directory, create it
    if not os.path.exists(dirname):
        os.makedirs(dirname)  

    for email_id in GetEmailIDs(service, email):
        DownloadEmail(service, email_id, dirname)
    
    print "finished emails for {}".format(email)

# Put emails to download here
DownloadEmails("sheila.shahmirza@collectivehealth.com")


##DownloadEmail(service, GetEmailIDs(service, "yourilicht@gmail.com")[0], "./")
