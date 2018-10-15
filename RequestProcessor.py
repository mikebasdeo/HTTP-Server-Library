import re
import os

test_regex = "^([^:\/\s\?]+ \/)?([^:\/\s\?]+)?"


def parse_request(request):

    request = request.decode()
    print("Request", request)
    matcher = re.search(test_regex, request)

    request_type = matcher.group(1)
    print("Request Type", request_type)


    if(request_type =='GET /'):

        
        if(matcher.group(2)):
            request_details = matcher.group(2)
            print("Request Details", request_details)
            f = open('%s.txt' % request_details, 'r')
            file_contents = f.read()
            return (file_contents)


        else:
            return str(os.listdir(os.getcwd() + '\data'))




        