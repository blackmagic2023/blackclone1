import os
from scapy.all import *

def packet_handler(packet):
    if packet.haslayer(Dot11):
        # Extract MAC addresses
        src_mac = packet.addr2
        dest_mac = packet.addr1

        # Extract SSID
        if packet.haslayer(Dot11Elt) and packet.type == 0 and packet.subtype == 8:
            ssid = packet[Dot11Elt].info.decode()

            # Display packet information
            print(f"SSID: {ssid}\tSource: {src_mac}\tDestination: {dest_mac}")

def start_sniffing(interface):
    try:
        # Put wireless adapter in monitor mode
        os.system(f"iwconfig {interface} mode monitor")
        print(f"[*] {interface} is now in monitor mode.")

        # Start sniffing packets
        sniff(iface=interface, prn=packet_handler)
    except KeyboardInterrupt:
        # Restore wireless adapter to managed mode
        os.system(f"iwconfig {interface} mode managed")
        print(f"\n[*] {interface} has been restored to managed mode.")
        exit(0)

if __name__ == "__main__":
    # Specify the wireless network interface (e.g., wlan0)
    wireless_interface = "wlan0"

    # Start sniffing packets
    start_sniffing(wireless_interface)
