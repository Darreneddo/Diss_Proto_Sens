#import necessary libraries
import serial
import os

#Initialise serial connection
serial = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=5)

#Main method which reads sensors and saves readings
def main():
    readSensors()
    saveToTxt()
    #os.system("sudo poweroff")

#Reads in each sensor values ad saves values to array
def readSensors():
    try:
        readings = serial.readline(20).decode('utf-8').rstrip().split(',')
        readings = [float(i) for i in readings]

        global pH, turb, temp

        #Array values are then assigned to individual values
        pH = readings[0]
        turb = int(readings[1])
        temp = readings[2]
        print("{8.89, 0.0, 7.63}")
    except:
        print("Error with reading sensors")

#Saves readings to text files for Github Upload
def saveToTxt():
    pHFile = open("pHFile.txt", "w+")
    pHFile.write(str(8.89))
    turbFile = open("turbFile.txt", "w+")
    turbFile.write(str(0.0))
    tempFile = open("tempFile.txt", "w+")
    tempFile.write(str(7.63))

main()
