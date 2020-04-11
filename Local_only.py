'''
this Program reads Speed Data from an UNO and
logs the data locally in a CSV File
'''
import serial, time, csv

port="/dev/ttyACM0"
global counter
counter=0


s1 = serial.Serial(port,115200)
s1.flushInput()

try:
    while (1):
            s1.inWaiting()>0
            input_data=s1.readline()  #reads the entire line until it sees \r or \n
            counter+=1
            try:
                decoded_data_1=(input_data[0:len(input_data)-2].decode("utf-8")) 
                decoded_data=float(input_data[0:len(input_data)-2].decode("utf-8"))  #cut of the \r\n and decode it
                print(decoded_data,'Kmph')
            except:
                continue
            if (counter%5==0):
                with open("Speed_local.csv",'a') as csvfile:
                    writer = csv.writer(csvfile,delimiter=",")
                    writer.writerow([time.ctime(),decoded_data,'kmph'])
except KeyboardInterrupt:
    pass
