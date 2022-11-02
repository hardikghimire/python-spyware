import pyscreenshot
import time
from datetime import datetime


while True:
    image = pyscreenshot.grab() # take screenshot

    cur_time = datetime.now().strftime('%b -%d -time -%I -%M -%S') # used to convert date and time objects to their string representation

    filename = cur_time + 'png' #save image according to time with adding .png extension

    image.save('<path>' + filename) # giving path to save the image

    time.sleep(7) # take screenshot in the gap of 7 second
