import sys, requests

try:
    macaddress = str(sys.argv[1])
except (IndexError, ValueError):
    print(f"\nMust supply an a mac-address as first argument\n")
    sys.exit(2)

template = 'https://api.macvendors.com/{}'
url = template.format(macaddress)
vendor = requests.get(url).text
print(f"\n{vendor}\n")