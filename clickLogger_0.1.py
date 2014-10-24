#!/usr/bin/python3
import time
import logging
import datetime as dt
import RPi.GPIO as gpio


logging.basicConfig(filename="logs/clicks2.log", fmt='%(asctime)s %(message)s', datefmt='%Y-%m-%d,%H:%M:%S.%f', level=logging.INFO)

gpio.VERSION
gpio.setmode(gpio.BOARD)
gpio.setup(7, gpio.IN)

timeStart = time.clock()
lastClick = timeStart
clickTotal = 0
maxTime=0
minTime = 1
avgTime = 0
elapseSum = 0



# from https://stackoverflow.com/questions/6290739/python-logging-use-milliseconds-in-time-format
class MyFormatter(logging.Formatter):
    converter=dt.datetime.fromtimestamp
    def formatTime(self, record, datefmt=None):
        ct = self.converter(record.created)
        if datefmt:
            s = ct.strftime(datefmt)
        else:
            t = ct.strftime("%Y-%m-%d %H:%M:%S")
            s = "%s,%03d" % (t, record.msecs)
        return s

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

console = logging.StreamHandler()
logger.addHandler(console)

formatter = MyFormatter(fmt='%(asctime)s %(message)s',datefmt='%Y-%m-%d,%H:%M:%S.%f')
console.setFormatter(formatter)

while (1):
	clickState = gpio.input(7)

	if clickState == 1:
		clickTime = time.clock()
		timeElapsed = clickTime - lastClick
		lastClick = clickTime
		clickTotal+=1
		if timeElapsed > maxTime:
			maxTime = timeElapsed

		if timeElapsed < minTime:
			minTime = timeElapsed

		avgTime = (elapseSum + timeElapsed) / clickTotal
		elapseSum += timeElapsed

		#print( "{} - Click detected".format( time.asctime() ))
		#print( "click detected: ",clickTime, timeElapsed, minTime, maxTime, avgTime, clickTotal)
		logger.info('click detected')
