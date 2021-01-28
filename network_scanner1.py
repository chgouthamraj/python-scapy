#!/usr/bin/env python3
import scapy.all as scapy
import optparse
#this funtion is used to take arguments
def get_arguments():
    parser=optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="target IP/Ip range")
    (options, arguments)=parser.parse_args()
    return options

def scan(ip):
#arp reuest is sent to specific ip
    arp_request=scapy.ARP(pdst=ip)
#broadcast macaddress is set to that it reaches all the clients/ether is a framework used for source and dest mac address
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#both are append for broadcast request
    arp_request_broadcat=broadcast/arp_request
#srp is used for sending and recieving request it returns two list answered and unanswered we make use of only answered
    answered_list=scapy.srp(arp_request_broadcat,  timeout=1, verbose=False)[0]
#answered list has sublists in it (packects, couples)
#appending directory into list
    client_list=[]
    for element in answered_list:
        client_dict={"ip":element[1].psrc,"mac":element[1].hwsrc}
        client_list.append(client_dict)
    return client_list

#this function is used to print results 
def print_result(result_list):
    print("Ip\t\t\tMAC Address ")
    print("---------------------------------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])

options=get_arguments()
scan_result = scan(options.target)
print_result(scan_result)
