#!/usr/bin/env python3.10

"""
This tool is still under development
 It is supposed to change the wifi name whenever you are connected to it.

 If you would like to contribute to this, reach out at Email: infosec947@gmail.com
"""
import pywifi
from pywifi import const

def change_wifi_ssid(new_ssid):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Assuming the first interface

    iface.disconnect()  # Disconnect from the current network

    profile = pywifi.Profile()
    profile.ssid = new_ssid  # Set the new SSID
    profile.auth = const.AUTH_ALG_OPEN  # Set authentication algorithm
    profile.key = "library@2023"  # Set the password for the network
    profile.akm.append(const.AKM_TYPE_WPA2PSK)  # Set security type to WPA2
    profile.cipher = const.CIPHER_TYPE_CCMP  # Set cipher type

    iface.remove_all_network_profiles()  # Remove existing profiles
    temp_profile = iface.add_network_profile(profile)  # Add the new profile

    iface.connect(temp_profile)  # Connect to the network with the new SSID

    # Wait for a while to ensure the connection is established
    import time
    time.sleep(20)

    if iface.status() == const.IFACE_CONNECTED:
        print(f"Successfully changed WiFi SSID to '{new_ssid}'")
    else:
        print("Failed to change WiFi SSID")
        print(f"Current Interface Status: {iface.status()}")

# xample usage: Change the SSID to 'myWifi'
new_ssid_name = 'myWifi'
change_wifi_ssid(new_ssid_name)
