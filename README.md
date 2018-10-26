

# Local Server Request

## Run echo server
`python echoserver.py --port 8007`

## Run echo server with debugging messages
`python echoserver.py -v -d "other" --port 8807`

## Change server data directory
`python echoserver.py -d "other" --port 8007`

## Httpc Get Command 
### Will return a list of the current files in the data directory.
`./httpc.py get localhost`

## Httpc Get /*
### Will return the contents of the fille named * inside the data directory.
`./httpc get localhost/foo`
 
## HTTPC Post /*
`./httpc post -d "Hello World" localhost/foo`






# Web Post Request
./httpc.py post -p 8007 -d "hello_world" http://httpbin.org/post
