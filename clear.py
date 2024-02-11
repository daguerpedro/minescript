import minescript
import time
import threading

lock = threading.Lock()

def clear(): 
    lock.acquire()    
    for i in range(500):
        minescript.echo('§r§k')   
    time.sleep(1)
    minescript.echo('§3Cleared messages.')
    lock.release()
    
clear()