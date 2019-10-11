#!/usr/bin/env python3
#hamid abdul
import time
import os
import subprocess
import configparser
import json
'''
put collected data into comma separated file
to use machine learning algorithms
'''
def outputFile():
   config = configparser.ConfigParser()
   x=open("/home/hamid/pyHS100/outfile.csv", "w")
   with open("/home/hamid/pyHS100/d.txt") as readFile:
       for i, line in enumerate(readFile):

           if "Time"  in line:
               x=line.split()
               t=x[1:3]
               for i in t:
                   print(i, end='')
               print("Time is ","\n",x[1:3])
               x.write(line)
           elif "voltage_mv" in line:
               print("line is ", line )
               x=json.dumps(line)
               print("print dump", x)
               y=json.loads(x)
               print("after",y)
               print(y['voltage_mv'])
               y=line.split()
               z=y[6:]
               for i in z:
                   print(i, end="")
               print(y[6:])
               x.write(line)

   readFile.close()
outputFile()



