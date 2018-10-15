import re
import os


# do some regex madness here instead.

def parse_request(request):
    request_type = request[:5]
    print("Request Type", request_type)

    if(request_type == b'GET /'):
        # Returns a list of the current files in the data directory
        return str(os.listdir(os.getcwd() + '\data'))