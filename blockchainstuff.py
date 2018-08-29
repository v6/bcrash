import requests
from block_io import BlockIo

#https://block.io/api/v2/get_balance/?api_key=BITCOIN

API_KEY='13cf-7f20-a5e8-5b05'
SECRET_PIN=''

r = requests.get('https://block.io/api/v2/get_balance/?api_key=' + API_KEY)

version = 2 # API
block_io = BlockIo(API_KEY, version)

block_io.get_new_address(label='basanese1')
