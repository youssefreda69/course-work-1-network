#from socket module we import  the required structures and constants
from socket import AF_INET, SOCK_STREAM, socket
#we will use the sleep function to keep application running
from time import sleep
#we will  need  the process id given by os when wew excute this code 
from os import getpid
#The Python interpreter examines the source file and defines a few special variables/global variables before running the code. The special __name__ variable is set to "__main__" 
if __name__ == '__main__':
    print('Application started')
    print('Os assigned process id: %d' %getpid())
#creating a TCP/UDP socket     
    s = socket(AF_INET, SOCK_STREAM)
    print('TCP Socket created')
    print('File descriptor assigned by OS:', s.fileno())
#binding the tcp socket   
    s.bind(('127.0.0.1', 7777))
    print('socket is bound to %s:%d' % s.getsockname())
    backlog = 0 
    s.listen(backlog)
    print('socket is in listening state to %s:%d' % s.getsockname())
    client_socket,client_addr = s.accept()
    print('New client connected from %s:%d' % client_addr)
    print('Local end-point socket bound on: %s:%d'% client_socket.getsockname())
    recv_buffer_length = 1024
    message = client_socket.recv(recv_buffer_length)
    print('Recieved %d bytes from %s:$%d' % ( (len(message),)+client_addr))
    print('Received message: \n%s' %message)
#waiting for user input before terminating application   
    input('press Enter to terminate....')
    wait_secs = 5
    print('Waiting %d seconds before termination ...' %wait_secs)
    sleep(wait_secs)
    print('Closing the TCP socket...')
    s.close()
    print('terminating....')