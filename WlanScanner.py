import ugfx
import badge
import network
strength = 0
if(ntwork_if = network.WLAN(network.STA_IF); sta_if.active(True)):
	for network in ntwork_if.scan():
		if(network[0].decode("ascii")==badge.nvs_get_str("badge","wifi.ssid",""):
			strength = network[3]
		
else:
	pass
	#do error handling here
