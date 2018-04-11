import requests
#copy right m4s_c0d3r
__banner__= """
	PROXY GENERATOR
  ___   ___   ___   ___   ___
 /   \ /   \ /   \ /   \ /   \  Author   : m4s_c0d3r
 | P | | R | | O | | X | | Y | 
 \___/ \___/ \___/ \___/ \___/ 	Team     : n4s
     ___      ___      ___
    /   \____/   \____/   \ 	Program	 : Python2
    | m |____| 4 |____| s |
    \___/    \___/    \___/ 	Facebook : https://www.facebook.com/bon
"""
url = 'https://api.getproxylist.com/proxy'

print __banner__
print ("This Free Proxy From getproxylist.com")
print("Generating Proxy...")


response = requests.get(url) 

data = response.json()

ip = data['ip']

print('IP/PORT		:'), ip,'/',data['port']
print('Protocol	:'), data['protocol']
print('Anonymity	:'), data['anonymity']
print('Last Tested	:'), data['lastTested']
print('Connect Time	:'), data['connectTime']
print('Speed		:'), data['downloadSpeed']
print('Ping		:'), data['secondsToFirstByte']
print('Country		:'), data['country']
