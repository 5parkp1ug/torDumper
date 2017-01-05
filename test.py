import urllib
data = []

url = urllib.urlopen('https://torstatus.blutmagie.de/query_export.php/Tor_query_EXPORT.csv')
dump = url.readlines()
dump.pop(0)

for line in dump:

	dict = {
		'ROUTER_NAME' : line.split(',')[0],
		'COUNTRY' : line.split(',')[1],
		'BANDWIDTH' : line.split(',')[2],
		'UPTIME' : line.split(',')[3],
		'IP_ADDR' : line.split(',')[4],
		'HOSTNAME' : line.split(',')[5],
		'OR_PORT' : line.split(',')[6],
		'DIR_PORT' : line.split(',')[7],
		'PLATFORM' : line.split(',')[17],
		'FIRST_SEEN' : line.split(',')[20],
		'AS_NAME' : line.split(',')[21],
		'AS_NUMBER' : line.split(',')[22],
		'C_BANDWIDTH' : line.split(',')[23],
		'OR_ADDR' : line.split(',')[24]
		}
	data.append(dict)
	
print data
