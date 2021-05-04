import serial
from time import sleep

# https://www.electronicwings.com/raspberry-pi/raspberry-pi-uart-communication-using-python-and-c

# GPIO 14 -> Tx
# GPIO 15 <- Rx

port = serial.Serial ("/dev/serial0", 115200)    #Open port with baud rate
while True:
    
    u = 'Hello World'
    b = bytes(u,'ascii')
    port.write(b)
    #received_data = port.read()              #read serial port
    line_data = port.readline(5)
    sleep(0.03)
    data_left = port.inWaiting()             #check for remaining byte
    #received_data += port.read(data_left)
    line_data += port.read(data_left)
    #print (received_data)                   #print received data
    print (line_data)
    #port.write(received_data)                #transmit data serially
    port.writelines(line_data)
    print ("Data transmitted successfully")
    