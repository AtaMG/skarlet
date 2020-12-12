#!/usr/bin/python3

import psutil 
import datetime
  
last_reboot = psutil.boot_time() 

up_time= datetime.datetime.now() - datetime.datetime.fromtimestamp(last_reboot)

if up_time.total_seconds() < 600 :
	print("System rebooted and Up time is less than 10 minutes")
