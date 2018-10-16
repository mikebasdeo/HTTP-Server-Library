import re
import os
import os.path
from pathlib import Path

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

            # todo error handling for file open/read
            my_file = Path("data/%s.txt" % request_details)
            if os.path.isfile(my_file):
                f = open(my_file, 'r')
                file_contents = f.read()
                print("made it here")
                return (file_contents)
                
            else:
                error_message = "Error 404: File Not Found"
                return(error_message)





        else:
            return str(os.listdir(os.getcwd() + '\data'))




        