#import 
import serial
import os

serial = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=5)

def main():
    readSensors()
    saveToTxt()
    #os.system("sudo poweroff")

def readSensors():
    try:
        readings = serial.readline(20).decode('utf-8').rstrip().split(',')
        readings = [float(i) for i in readings]

        global pH, turb, temp

        pH = readings[0]
        turb = int(readings[1])
        temp = readings[2]
        print(readings)
    except:
        print("Error with reading sensors")

def saveToTxt():
    pHFile = open("pHFile.txt", "w+")
    pHFile.write(str(pH))
    turbFile = open("turbFile.txt", "w+")
    turbFile.write(str(turb))
    tempFile = open("tempFile.txt", "w+")
    tempFile.write(str(temp))

main()
