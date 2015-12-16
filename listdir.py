import commands
import sys
import os

def List(dir):
	cmd = 'ls -l ' + dir
	print "Command to run:", cmd
	(status, output) = commands.getstatusoutput(cmd)
	print output

List("~/Desktop")