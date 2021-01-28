#!/usr/bin/env python
import netfilterqueue

#packet.accept() is used to forward packets to destitation from queue /packet.drop() is used to drop packets
def process_packet(packet):
        print(packet)
        packet.drop()


queue=netfilterqueue.NetfilterQueue()
#this will bind our queue which we created in terminal/call hack function on each packet
queue.bind(0, process_packet)
queue.run()

