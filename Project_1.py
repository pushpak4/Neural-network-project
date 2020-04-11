'''
This program reads the Speed from an UNO and
posts the data locally in a CSV file and on
www.thingspeak.com
'''
import serial, time, csv
import urllib.request
import urllib.parse

Tp_key = 'SVDTA6LLQVLG2WPK'
Tp_url = 'https://api.thingspeak.com/update'
port="/dev/ttyACM0"
baud = 115200
global counter
counter=0

s1 = serial.Serial(port,baud)
s1.flushInput()

def postData(url,key,field1,speed):
    try:
        values = {'api_key' : key,'field1' : speed}
        postdata = urllib.parse.urlencode(values)
        postdata = postdata.encode('utf-8')
        req = urllib.request.Request(url, postdata)
        response = urllib.request.urlopen(req, None, 2)
        #html_string = response.read()
        response.close()

    except Exception as e:
        print(str(e))


try:
    while (1):
        s1.inWaiting()>0
        input_data=s1.readline()  #reads the entire line until it sees \r or \n
        counter+=1;
        try:
            #decoded_raw=(input_data[0:len(input_data)-2].decode("utf-8")) 
            decoded_speed=float(input_data[0:len(input_data)-2].decode("utf-8"))  #cut of the \r\n and decode it
            print(decoded_speed, 'Kmph')
        except:
            continue
        with open("Speed.csv",'a') as csvfile:
            writer = csv.writer(csvfile,delimiter=",")
            writer.writerow([time.ctime(),decoded_speed])
            if (float(decoded_speed)>300.00):
                if (counter%10==0):
                    postData(Tp_url,Tp_key,'field1',decoded_speed)

except KeyboardInterrupt:
    pass

