#!/usr/bin/python3
import time
import logging
import datetime as dt
import RPi.GPIO as gpio

# baseline conversion information for Clicks-per-second (CPS) to uSv: https://sites.google.com/site/diygeigercounter/gm-tubes-supported
# the MightyOhm shipped with a SBM-20 tube


clickLogger = logging.getLogger('click_logger')
clickLogger.setLevel(logging.INFO)

fh = logging.FileHandler("logs/clicks.log")
fh.setLevel(logging.INFO)

ch = logging.StreamHandler();
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s.%(msecs)d %(message)s', datefmt='%Y-%m-%d,%H:%M:%S')

#fh.setFormatter(formatter)
#ch.setFormatter(formatter)

clickLogger.addHandler(fh)
clickLogger.addHandler(ch)

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
		#clickTime = time.clock()
		#clickTime = time.time() # we want to ge microsecond resolution from the posix timestamp value
		clickTime = time.time() + datetime.timedelta(days=3).total_seconds()
		#timeElapsed = clickTime - lastClick
		#lastClick = clickTime
		#clickTotal+=1
		#if timeElapsed > maxTime:
		#	maxTime = timeElapsed
		#
		#if timeElapsed < minTime:
		#	minTime = timeElapsed
		#
		#avgTime = (elapseSum + timeElapsed) / clickTotal
		#elapseSum += timeElapsed

		#print( "{} - Click detected".format( time.asctime() ))
		#print( "click detected: ",clickTime, timeElapsed, minTime, maxTime, avgTime, clickTotal)
		#logger.info('click detected')
		clickLogger.info(clickTime)