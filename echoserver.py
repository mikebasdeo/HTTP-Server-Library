import socket
import threading
import RequestProcessor
import argparse


def run_server(host, port):
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        listener.bind((host, port))
        listener.listen(5)
        print('Echo server is listening at', port)
        while True:
            conn, addr = listener.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()
    finally:
        listener.close()


def handle_client(conn, addr):
    print ('New client from', addr)
    try:
        while True:
            data = conn.recv(1024)
            response_to_return = RequestProcessor.parse_request(data)
            if not data:
                break
            conn.sendall(response_to_return.encode())
            break
    finally:
        conn.close()

parser = argparse.ArgumentParser()
parser.add_argument("--port", help="echo server port", type=int, default=8007)
parser.add_argument('-d', dest="data", action="store", metavar="inline-data", help="Specifies the directory the server will use to read/write. Default is the current directory.")
parser.add_argument('-v','--verbose', action="store_true")

args = parser.parse_args()

# handles directory change
RequestProcessor.setDirectory("data")
if(args.data):
    RequestProcessor.setDirectory(args.data)
if (args.verbose):
    RequestProcessor.setVerbose()
    


run_server('', args.port)


