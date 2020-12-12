#!/usr/bin/python3

import subprocess

def cmd(command):
	try:
		res = subprocess.run(command.split(), capture_output=True, text=True)
		print("Docker is installed,", res.stdout)
        
	except:
		print("Docker is not installed.")

cmd("docker -v")


