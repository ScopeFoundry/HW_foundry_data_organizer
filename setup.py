from setuptools import setup

setup(
    name = 'ScopeFoundryHW.foundry_data_organizer',
    
    version = '0.0.1',
    
    description = 'ScopeFoundry Hardware plug-in: Proposal ID metadata capture',
    
    # Author details
    author='Morgan K Wall',
    author_email='mkwall@lbl.gov',

    # Choose your license
    license='BSD',

    package_dir={'ScopeFoundryHW.foundry_data_organizer': '.'},
    
    packages=['ScopeFoundryHW.foundry_data_organizer',],
        
    package_data={
        '':["README*", 'LICENSE', # include License and readme 
            "*.ui", # include QT ui files 
            ], 
        },
    )