# Requirements
1. Python 3+

# Run echo server

`python echoserver.py --port 8007`

# Httpc Get Command 
## Will return a list of the current files in the data directory.
./httpc.py get localhost

# Httpc Get/*
## Will return the contents of the fille named * inside the data directory.
./httpc get localhost/foo


# Mike's Notes
`python httpc.py get localhost`