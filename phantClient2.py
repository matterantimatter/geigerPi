#!/usr/bin/python
from phant import Phant

p = Phant('v8bxxz3EVJIWV3gwaR2ahRZDyD7e', 'clickTime', base_url='http://192.168.1.64:8080',  private_key='KM2KKX5yYaSmy8A9dLgdu19e7exV')

p.log(33.4)
print(p.remaining_bytes, p.cap)

data = p.get()
print(data['clickTime'])
