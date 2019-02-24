import requests

session = None

# User settable options
API_KEY = None
API_PATH = 'http://politicsandwar.com/api'
def load(**kwargs):
    if 'key' in kwargs:
        global API_KEY
        API_KEY = kwargs['key']

    if 'test_server' in kwargs:
        global API_PATH
        if kwargs['test_server'] == True:
            API_PATH = 'http://test.politicsandwar.com/api'
        else:
            API_PATH = 'http://politicsandwar.com/api'
    else:
        API_PATH = 'http://politicsandwar.com/api'

    # Create a requests session and set API key if applicable
    global session
    session = requests.Session()
    if API_KEY is not None:
        session.params = {
            'key': API_KEY
        }

# Imports
from .nation import Nation
from .alliance import Alliance
