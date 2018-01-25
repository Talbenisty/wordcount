import re
import pdb


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
    BodyWithoutQuotedText = remove_quote(BodyInLines)

    return BodyWithoutQuotedText

def is_timestamp(line):
 	return re.match('^On (.*)> wrote:$', line) != None

def remove_quote(body):
	quoteless_body = [] 
	for line in body:
		if is_timestamp(line):
			break
		else: 
			quoteless_body.append(line)

	return "".join(quoteless_body)



  	