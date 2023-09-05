import numpy as np
import time

class DataOrganizerDevice(object):
    """
    This is the low level dummy device object.
    Typically when instantiated it will connect to the real-world
    Methods allow for device read and write functions
    """
        
    def __init__(self):
        """We would connect to the real-world here
        if this were a real device
        """
        self.request_pid()

    def request_pid(self):
        pid = input("What is your proposal ID?")
        if pid == "":
            self._pid = "unknown"
        else:
            self._pid = pid

    def write_pid(self, pid):
        """
        A write function to change the device's amplitude
        normally this would talk to the real-world to change
        a setting on the device
        """

        self._pid = pid
            
    
        