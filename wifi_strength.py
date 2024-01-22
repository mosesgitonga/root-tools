#!/usr/bin/env python3.10
"""
Measures the strength of wifi and its speed
"""
import pywifi
from pywifi import const
import speedtest


class Color:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'

def get_bandwidth(freq):
    # Returns the bandwidth based on frequency
    if freq < 5000:
        return "2.4 GHz"
    else:
        return "5 GHz"

def test_speed():
    # Perform speed test using speedtest-cli
    st = speedtest.Speedtest()
    st.get_best_server()

    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps

    return download_speed, upload_speed

wifi = pywifi.PyWiFi()

iface = wifi.interfaces()[0]  # Assuming the first interface

iface.scan()
results = iface.scan_results()

for wifi_network in results:
    print(f"{Color.RED}SSID{Color.RESET}: {Color.GREEN}{wifi_network.ssid}{Color.RESET}\n{Color.YELLOW} Signal Strength{Color.RESET}: {Color.GREEN}{wifi_network.signal}{Color.RESET}\n {Color.YELLOW}Bandwidth:{Color.RESET}{Color.YELLOW} {get_bandwidth(wifi_network.freq)}{Color.RESET}")
    # Test speed for each network
    print(f"{Color.BLUE}Please wait.\nChecking Download and Upload speed...\nThis might take a minute{Color.RESET}")

    download_speed, upload_speed = test_speed()
    print(f"{Color.YELLOW}Download Speed:{Color.RESET} {Color.GREEN}{download_speed:.2f} Mbps \n{Color.GREEN} Upload Speed:{Color.RESET} {Color.YELLOW}{upload_speed:.2f} {Color.GREEN}Mbps{Color.RESET}")
    
