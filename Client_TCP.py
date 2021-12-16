#from socket module we import the required structures and constants
from socket import AF_INET, SOCK_STREAM, socket
#we will use the sleep function to keep application running
from time import sleep
#we will need the process id given by os when wew excute this code 
from os import getpid
#The Python interpreter examines the source file and defines a few special variables/global variables before running the code. The special __name__ variable is set to "__main__" 
if __name__ == '__main__':
    print('Application started')
    print('Os assigned process id: %d' %getpid())
#creating a TCP socket   
    s = socket(AF_INET, SOCK_STREAM)
    print('TCP Socket created')
    print('File descriptor assigned by OS:', s.fileno())
# no binding needed from the client the os will bind automatically    
    server_address = ('127.0.0.1',7777)
    s.connect(server_address)  
    print('socket is connected to %s:%d' % s.getpeername())
    print('Local end-point is bound to %s:%d' % s.getsockname())
    message = 'Hello world'
    if s.sendall(message.encode()) == None:
        print('Send %d bytes to %s:%d' % ((len(message),)+s.getpeername()))
#waiting for user input before terminating application      
    input('press Enter to terminate....') 
    wait_secs = 5 
    print('Waiting %d seconds before termination ...' %wait_secs) 
    sleep(wait_secs) 
    print('Closing the TCP socket...') 
    s.close()
    print('terminating....') 