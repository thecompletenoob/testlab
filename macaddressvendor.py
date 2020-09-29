import sys, requests

try:
    macaddress = str(sys.argv[1])
except (IndexError, ValueError):
    print('Must supply an a mac-address as first argument')
    sys.exit(2)

template = 'https://api.macvendors.com/{}'
url = template.format(macaddress)
vendor = requests.get(url).text
print(vendor)