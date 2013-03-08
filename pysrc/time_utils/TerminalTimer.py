'''
Created on Mar 8, 2013

@author: shaked
'''
import time
import sys

def remain_clock():

    for remaining in range(10, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining)) 
        sys.stdout.flush()
        time.sleep(1)
    
    sys.stdout.write("\rComplete!            \n")
    
