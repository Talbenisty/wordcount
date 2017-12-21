

from CleanABody import CleanABody
from Gmail import ListMessagesMatchingQuery
from Gmail import GetMessageBody
from Gmail import GetService
from Gmail import GetEmailIDs


service = GetService()






##ListofEmailIDs = ListMessagesMatchingQuery(service, "me", "from:sarahroseklearman@gmail.com")


##NewListOfEmailIDs = [GrabEmailID(x) for x in ListofEmailIDs]

##NewListOfBodies = [CleanABody(x) for x in NewListOfEmailIDs]


def CleanListOfBodies(EmailAddress): 

    ListofEmailData = ListMessagesMatchingQuery(service, "me", "from:{}".format(EmailAddress))
    
    ListOfEmailIDs = [x['id'] for x in ListofEmailData]


    ListOfBodies = [GetMessageBody(service, "me", x) for x in ListOfEmailIDs]

    CleanBodies = [CleanABody(x) for x in ListOfBodies]

    return CleanBodies


##print(CleanListOfBodies("sheila.shahmirza@collectivehealth.com"))


def IDToFile (EmailID):

	EmailBody = GetMessageBody(service, "me", EmailID)
	CleanBody = CleanABody(EmailBody)

	CreateEmailTextFile = open("{}.txt".format(EmailID), "wb")
	CreateEmailTextFile.write("\n".join(CleanBody))

	print("Done")


ListofEmailData = GetEmailIDs(service, "sheila.shahmirza@collectivehealth.com")

FirstEmailData = ListofEmailData[0]

print(ListofEmailData)

##IDToFile(GrabEmailID(FirstEmailData))


##To DO##
##Move EmailID to Gmail helper
##Save all the emails in a directory















