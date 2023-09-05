from ScopeFoundry import HardwareComponent
from ScopeFoundryHW.foundry_data_organizer.foundry_data_organizer_device import DataOrganizerDevice


class DataOrganizerHW(HardwareComponent):
    
    ## Define name of this hardware plug-in
    name = 'data_organizer'
    
    def setup(self):
        # Define your hardware settings here.
        # These settings will be displayed in the GUI and auto-saved with data files
        self.settings.New('proposal_id', dtype=str, initial="0000")
        
        # this will run when you start your application
        #self.settings.proposal_id = input("please enter your pid")

    def connect(self):
        # Open connection to the device:
        self.data_org_dev = DataOrganizerDevice()
        
        # Connect settings to hardware:
        self.settings.proposal_id.connect_to_hardware(
            write_func = self.data_org_dev.request_pid
           )
        
    def disconnect(self):
        # remove all hardware connections to settings
        self.settings.disconnect_all_from_hardware()
        
        # Don't just stare at it, clean up your objects when you're done!
        if hasattr(self, 'data_org_dev'):
            del self.data_org_dev