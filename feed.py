import minescript
import time
import threading
import random

lock = threading.Lock()
command = '/feed'

def feed(): 
    minescript.echo('[§2+§r] §eStarting autofeed.')
    lock.acquire()    
    while(minescript.world_properties()['address'] == 'EXAMPLE.SERVER.IP' or minescript.world_properties()['address'] == 'localhost'):
        minescript.execute(command)
        minescript.echo('[§2+§r] §eSuccessfully feed.')
        time.sleep(random.randrange(1 * 60, 5 * 60))
        
    lock.release()
    
    time.sleep(5)
    
    feed()
    
feed()
