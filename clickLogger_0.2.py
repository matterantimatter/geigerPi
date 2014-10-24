#!/usr/bin/python3
import time
import logging
import datetime as dt
import RPi.GPIO as gpio


logging.basicConfig(filename="logs/clicks2.log", format='%(asctime)s %(message)s', datefmt='%Y-%m-%d,%H:%M:%S.%f', level=logging.INFO)

clickLogger = logging.getLogger('click_logger')
clickLogger.setLevel(logging.INFO)

fh = logging.FileHandler("logs/clicks.log")
fh.setLevel(logging.INFO)

ch = logging.StreamHandler();
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s %(message)s', datefmt='%Y-%m-%d,%H:%M:%S.%f')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

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
		#print( "click detected: ",clickTime, timeElapsed, minTime, maxTime, avgTime, clickTotal)
		#logger.info('click detected')
		clickLogger.info("click_detected")
		fh.info("click")
		ch.info("click")
