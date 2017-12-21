def RemoveBreaklines(body):
     return body.replace('=\r\n','')

def ConvertBodyToLines(body):
     return body.split('\r\n')

def IsQuoteLine(bodyLine): 
     return bodyLine.startswith(">") 

def RemoveQuotes(body):
     return filter(lambda x: not IsQuoteLine(x),body)

##takes a multiline string and returns a list of unquoted lines
def CleanABody(body):

    BodyWithoutBreaklines = RemoveBreaklines(body)
    BodyInLines = ConvertBodyToLines(BodyWithoutBreaklines)
    BodyWithoutQuotedText = RemoveQuotes(BodyInLines)

    return BodyWithoutQuotedText