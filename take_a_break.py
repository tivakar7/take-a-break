import webbrowser
import time
import sys

if(len(sys.argv) == 1):
	print "Invalid input \n Usage: python take_a_break.py <Break Interval in sec>"
	exit(0);

var =1
while(var == 1):
    time.sleep(int(sys.argv[1]))
    webbrowser.open("http://www.brainyquote.com/quotes_of_the_day.html")  
    

    

