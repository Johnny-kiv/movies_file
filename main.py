import os 
import time
while True:
    os.rename("./templates/index.html","./index.html")
    time.sleep(1)
    os.replace("./index.html","./templates/index.html")
    time.sleep(1)