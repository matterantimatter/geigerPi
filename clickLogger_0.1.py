#!/usr/bin/python3
import time
import logging
import RPi.GPIO as gpio

logging.basicConfig(filename="logs/clicks.log", level=logging.info)

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
		print( "click detected: ",clickTime, timeElapsed, minTime, maxTime, avgTime, clickTotal)
