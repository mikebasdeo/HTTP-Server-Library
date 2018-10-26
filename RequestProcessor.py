import re
import os
import sys
import os.path
from pathlib import Path

#test_regex = "^([^:\/\s\?]+ \/)?([^:\/\s\?]+)?"
test_regex = r"^([^:\/\s\?]+ \/)?([^:\/\s\?]+)?(.*\s.*)*(\s\s)(.*)?"

def parse_request(request):

    request = request.decode()
    print("Request", request)
    matcher = re.search(test_regex, request)

    request_type = matcher.group(1)


    if(request_type=='POST /'):
        print("Fucking Request", request)
        # get file
        request_details = matcher.group(2)

        print("Fucking Request Details", request_details)

        # get data
        request_data = matcher.group(3)
        print("Request Data to put in file", request_data)
        # put data in file
        my_file = Path("data/%s.txt" % request_details)
        if os.path.isfile(my_file):
            f = open(my_file, 'w')
            f.write(request_data)            
        else:
            error_message = "Error 6969 Writing to file error"
            return(error_message)








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
            return str(os.listdir(os.getcwd() + r'\data'))




        