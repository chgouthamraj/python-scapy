#!/usr/bin/env python3
import scapy.all as scapy

def scan(ip):
    arp_request=scapy.ARP(pdst=ip)
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcat=broadcast/arp_request
    answered_list=scapy.srp(arp_request_broadcat,  timeout=1, verbose=False)[0]
    print("Ip\t\t\tMAC Address ")
    print("---------------------------------------------------")
    client_list=[]
    for element in answered_list:
        client_dict={"ip":element[1].psrc,"mac address":element[1].hwsrc}
        client_list.append(client_dict)
        print(element[1].psrc +"\t"+"|"+"\t"+ element[1].hwsrc)
    print(client_list)


scan("10.0.2.15/24")
