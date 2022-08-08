# !/usr/bin/python

"""
Task 1: Implementation of the experiment described in the paper with title: 
"From Theory to Experimental Evaluation: Resource Management in Software-Defined Vehicular Networks"
http://ieeexplore.ieee.org/document/7859348/ 
"""

import os
import time
import matplotlib.pyplot as plt
from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch, OVSKernelAP
from mininet.link import TCLink
from mininet.log import setLogLevel, debug
from mininet.cli import CLI

import sys
gnet=None

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Adding the latencies from car0-car3 and car3-client ping results
def add():

    car0_ping = 'car0_ping.data'
    car3_ping = 'car3_ping.data'

    f1 = open('./'+car0_ping, 'r')
    car0 = f1.readlines()
    f1.close()

    f2 = open('./'+car3_ping, 'r')
    car3 = f2.readlines()
    f2.close()

    f3 = open('./car0.data', 'w')
    i = 0
    for x in car0:
        if(len(x) is 7):
            break
        p = x.split('=')
        print >> f3, float(p[1])
    f3.close()

    f4 = open('./car3.data', 'w')
    i = 0
    for x in car3:
        if(len(x) is 7):
            break
        p = x.split('=')
        print >> f4, float(p[1])
    f4.close()

    print "telos"

    f3 = open('./car0.data', 'r')
    car0 = f3.readlines()
    f3.close()
    
    f4 = open('./car3.data', 'r')
    car3 = f4.readlines()
    f4.close()

    f5 = open('./latency.data', 'w')

    i=0
    for x in car0:
        result = float(x)+float(car3[i])
        print >> f5, result
        i += 1

    f5.close()

    os.system('rm car0.data')
    os.system('rm car3.data')
    os.system('rm car0_ping.data')
    os.system('rm car3_ping.data')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# "cleans" the files with car0-clients's ping results so that there are only the latency time
def clean_latency():

    p2 = 'phase2.data'
    p3 = 'phase3.data'

    f1 = open('./'+p2, 'r')
    phase2 = f1.readlines()
    f1.close()

    f2 = open('./'+p3, 'r')
    phase3 = f2.readlines()
    f2.close()

    f3 = open('./latency.data', 'a')
    i = 0
    for x in phase2:
        if(len(x) is 12):
            break
        p = x.split('=')
        print >> f3, float(p[1])

    i = 0
    for x in phase3:
        if(len(x) is 7):
            break
        p = x.split('=')
        print >> f3, float(p[1])
    f3.close()

    os.system('rm phase2.data')
    os.system('rm phase3.data')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# "cleans" the files with car0's and switch's packets and throughput, so that there are only the packets
def cleaning():

    c0_pkt = 'packets_car0.data'
    switch_pkt = 'packets_switch.data'
    c0_throughput = 'throughput_car0.data'
    switch_throughput = 'throughput_switch.data'


    f1 = open('./' + switch_pkt, 'r')
    spkt = f1.readlines()
    f1.close()

    f11 = open('./' + switch_throughput, 'r')
    sthr = f11.readlines()
    f11.close()

    f2 = open('./' + c0_pkt, 'r')
    cpkt = f2.readlines()
    f2.close()

    f21 = open('./' + c0_throughput, 'r')
    cthr = f21.readlines()
    f21.close()

    f1 = open('./snum.data', 'w')
    i = 0
    for x in spkt:
        p = x.split(':')
        print >> f1, int(p[1])
    f1.close()

    f11 = open('./sthrnum.data', 'w')
    i = 0
    for x in sthr:
        p = x.split(':')
        print >> f11, int(p[1])
    f11.close()

    f2 = open('./cnum.data', 'w')
    i = 0
    for x in cpkt:
        p = x.split(':')
        print >> f2, int(p[1])
    f2.close()

    f21 = open('./cthrnum.data', 'w')
    i = 0
    for x in cthr:
        p = x.split(':')
        print >> f21, int(p[1])
    f21.close()

    os.system('rm packets_car0.data')
    os.system('rm packets_switch.data')
    os.system('rm throughput_car0.data')
    os.system('rm throughput_switch.data')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Implement the graphic function in order to demonstrate the network measurements
# Hint: You can save the measurement in an output file and then import it here
def graphic():

    cleaning()

    a = 'snum.data'
    b = 'sthrnum.data'
    c = 'cnum.data'
    d = 'cthrnum.data'

    f1 = open('./'+a, 'r')
    spkt = f1.readlines()
    f1.close()

    f11 = open('./'+b, 'r')
    sthr = f11.readlines()
    f11.close()

    f2 = open('./'+c, 'r')
    cpkt = f2.readlines()
    f2.close()

    f21 = open('./'+d, 'r')
    cthr = f21.readlines()
    f21.close()

    # initialize some variable to be lists:
    l1 = []
    l2 = []
    ll1 = []
    ll2 = []
    t1 = []
    t2 = []
    tt1 = []
    tt2 = []
    t = []

    # scan the rows of the file stored in lines, and put the values into some variables:
    i = 0
    for x in spkt:
        l1.append(int(x))

        if len(l1) > 1:
            ll1.append(l1[i] - l1[i - 1])
            i += 1

    i = 0
    for x in sthr:
        t1.append(int(x))

        if len(t1) > 1:
            tt1.append(t1[i] - t1[i - 1])
            i += 1

    i = 0
    for x in cpkt:
        l2.append(int(x))

        if len(l2) > 1:
            ll2.append(l2[i] - l2[i - 1])
            i += 1


    i = 0
    for x in cthr:
        t2.append(int(x))

        if len(t2) > 1:
            tt2.append(t2[i] - t2[i - 1])
            i += 1


    i = 0
    for x in range(len(ll1)):
        t.append(i)
        i += 1

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    ax1.plot(t, ll1, color='red', label='Received Data (client)', ls="--", markevery=7, linewidth=1)
    ax1.plot(t, ll2, color='black', label='Transmited Data (server)', markevery=7, linewidth=1)
    ax2.plot(t, tt1, color='red', label='Throughput (client)', ls="-.", markevery=7, linewidth=1)
    ax2.plot(t, tt2, color='black', label='Throughput (server)', ls=':', markevery=7, linewidth=1)
    ax1.legend(loc=2, borderaxespad=0., fontsize=12)
    ax2.legend(loc=1, borderaxespad=0., fontsize=12)


    ax2.set_yscale('log')

    ax1.set_ylabel("# Packets (unit)", fontsize=18)
    ax1.set_xlabel("Time (seconds)", fontsize=18)
    ax2.set_ylabel("Throughput (bytes/sec)", fontsize=18)

    plt.show()

    plt.savefig("Throughput.png")

    CLI(gnet)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def latency_graph():

    file = 'latency.data'

    f1 = open('./'+file, 'r')
    late = f1.readlines()
    f1.close()

    t = []

    i = 0
    for x in range(len(late)):
        t.append(i)
        i += 1

    fig, ax = plt.subplots()

    ax.plot(t, late, color='magenta', label='Latency (network)', ls="--", markevery=7, linewidth=1)
    ax.legend(loc=1, borderaxespad=0., fontsize=12)
    ax.set_ylabel("Latency (ns)", fontsize=18)
    ax.set_xlabel("Time (seconds)", fontsize=18)

    plt.show()

    plt.savefig("Latency.png")

    CLI(gnet)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def apply_experiment(car,client,switch):
    
    c0_pkt = 'packets_car0.data'
    switch_pkt = 'packets_switch.data'
    c0_throughput = 'throughput_car0.data'
    switch_throughput = 'throughput_switch.data'

    #time.sleep(2)
    print "Applying first phase"

    ################################################################################ 
    #   1) Add the flow rules below and the necessary routing commands
    #
    #   Hint 1: For the OpenFlow rules you can either delete and add rules
    #           or modify rules (using mod-flows command)       
    #   Example: os.system('ovs-ofctl mod-flows switch in_port=1,actions=output:2')
    #
    #   Hint 2: For the routing commands check the configuration 
    #           at the beginning of the experiment.
    #
    #   2) Calculate Network Measurements using IPerf or command line tools(ifconfig)
    #       Hint: Remember that you can insert commands via the mininet
    #       Example: car[0].cmd('ifconfig bond0 | grep \"TX packets\" >> %s' % output.data)
    #
    #               ***************** Insert code below *********************  
    #################################################################################

    os.system('ovs-ofctl mod-flows switch in_port=1,actions=output:4')
    os.system('ovs-ofctl mod-flows switch in_port=4,actions=output:1')
    os.system('ovs-ofctl mod-flows switch in_port=2,actions=drop')
    os.system('ovs-ofctl mod-flows switch in_port=3,actions=drop')
    os.system('ovs-ofctl del-flows eNodeB1')
    os.system('ovs-ofctl del-flows eNodeB2')
    os.system('ovs-ofctl del-flows rsu1')
 
    car[0].cmd('ip route add 200.0.10.2 via 200.0.10.50')
    client.cmd('ip route add 200.0.10.100 via 200.0.10.150')

    for i in range(0,20):
        car[0].cmd('ifconfig bond0 | grep \"TX packets\" | awk -F \' \' \'{print $2}\' >> %s' % c0_pkt)
        switch.cmd('ifconfig switch-eth4 | grep \"TX packets\" | awk -F \' \' \'{print $2}\' >> %s' % switch_pkt)
        car[0].cmd('ifconfig bond0 | grep \"bytes\" | awk -F \' \' \'{print $6}\' >> %s' % c0_throughput)
        switch.cmd('ifconfig switch-eth4 | grep \"bytes\" | awk -F \' \' \'{print $6}\'>> %s' % switch_throughput)
        time.sleep(1)

    car[0].cmd('ping 10.0.0.4 -c 10 | grep \"time\" | awk -F \' \' \'{print $7}\' >> car0_ping.data')
    car[3].cmd('ping 200.0.10.2 -c 10 | grep \"time\" | awk -F \' \' \'{print $7}\' >> car3_ping.data')

    add()

    CLI(gnet)

    print "Moving nodes"
    car[0].moveNodeTo('150,100,0')
    car[1].moveNodeTo('120,100,0')
    car[2].moveNodeTo('90,100,0')
    car[3].moveNodeTo('70,100,0')

    
    #time.sleep(2)
    print "Applying second phase"
    ################################################################################ 
    #   1) Add the flow rules below and the necessary routing commands
    #
    #   Hint 1: For the OpenFlow rules you can either delete and add rules
    #           or modify rules (using mod-flows command)       
    #   Example: os.system('ovs-ofctl mod-flows switch in_port=1,actions=output:2')
    #
    #   Hint 2: For the routing commands check the configuration 
    #           you have added before.
    #           Remember that now the car connects to RSU1 and eNodeB2
    #
    #   2) Calculate Network Measurements using IPerf or command line tools(ifconfig)
    #       Hint: Remember that you can insert commands via the mininet
    #       Example: car[0].cmd('ifconfig bond0 | grep \"TX packets\" >> %s' % output.data)
    #
    #           ***************** Insert code below ********************* 
    #################################################################################
    
    os.system('ovs-ofctl mod-flows switch in_port=1,actions=drop')
    os.system('ovs-ofctl mod-flows switch in_port=2,actions=output:4')
    os.system('ovs-ofctl mod-flows switch in_port=4,actions=output:2,3')
    os.system('ovs-ofctl mod-flows switch in_port=3,actions=output:4')
    os.system('ovs-ofctl del-flows eNodeB1')
    os.system('ovs-ofctl del-flows eNodeB2')
    os.system('ovs-ofctl del-flows rsu1')

    car[0].cmd('ip route del 200.0.10.2 via 200.0.10.50')
    client.cmd('ip route del 200.0.10.100 via 200.0.10.150')

    for i in range(0,20):
        car[0].cmd('ifconfig bond0 | grep \"TX packets\" | awk -F \' \' \'{print $2}\' >> %s' % c0_pkt)
        switch.cmd('ifconfig switch-eth4 | grep \"TX packets\" | awk -F \' \' \'{print $2}\' >> %s' % switch_pkt)
        car[0].cmd('ifconfig bond0 | grep \"bytes\" | awk -F \' \' \'{print $6}\' >> %s' % c0_throughput)
        switch.cmd('ifconfig switch-eth4 | grep \"bytes\" | awk -F \' \' \'{print $6}\'>> %s' % switch_throughput)
        time.sleep(1)
    
    car[0].cmd('ping 200.0.10.2 -c 10 | grep \"time\" | awk -F \' \' \'{print $7}\' >> phase2.data')

    CLI(gnet)

    print "Moving nodes"
    car[0].moveNodeTo('190,100,0')
    car[1].moveNodeTo('150,100,0')
    car[2].moveNodeTo('120,100,0')
    car[3].moveNodeTo('90,100,0')

    
    #time.sleep(2)
    print "Applying third phase"
    
    ################################################################################ 
    #   1) Add the flow rules below and routing commands if needed
    #
    #   Hint 1: For the OpenFlow rules you can either delete and add rules
    #           or modify rules (using mod-flows command)       
    #   Example: os.system('ovs-ofctl mod-flows switch in_port=1,actions=output:2')
    #
    #
    #   2) Calculate Network Measurements using IPerf or command line tools(ifconfig)
    #       Hint: Remember that you can insert commands via the mininet
    #       Example: car[0].cmd('ifconfig bond0 | grep \"TX packets\" >> %s' % output.data)
    #
    #           ***************** Insert code below ********************* 
    #################################################################################

    os.system('ovs-ofctl mod-flows switch in_port=1,actions=drop')
    os.system('ovs-ofctl mod-flows switch in_port=3,actions=drop')
    os.system('ovs-ofctl mod-flows switch in_port=2,actions=output:4')
    os.system('ovs-ofctl mod-flows switch in_port=4,actions=output:2')
    os.system('ovs-ofctl del-flows eNodeB1')
    os.system('ovs-ofctl del-flows eNodeB2')
    os.system('ovs-ofctl del-flows rsu1')

    for i in range(0,20):
        car[0].cmd('ifconfig bond0 | grep \"TX packets\" | awk -F \' \' \'{print $2}\' >> %s' % c0_pkt)
        switch.cmd('ifconfig switch-eth4 | grep \"TX packets\" | awk -F \' \' \'{print $2}\' >> %s' % switch_pkt)
        car[0].cmd('ifconfig bond0 | grep \"bytes\" | awk -F \' \' \'{print $6}\' >> %s' % c0_throughput)
        switch.cmd('ifconfig switch-eth4 | grep \"bytes\" | awk -F \' \' \'{print $6}\'>> %s' % switch_throughput)
        time.sleep(1)

    car[0].cmd('ping 200.0.10.2 -c 10 | grep \"time\" | awk -F \' \' \'{print $7}\' >> phase3.data')

    clean_latency()

    CLI(gnet)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def topology():
    "Create a network."
    net = Mininet(controller=Controller, link=TCLink, switch=OVSKernelSwitch, accessPoint=OVSKernelAP)
    global gnet
    gnet = net

    print "*** Creating nodes"
    car = []
    stas = []
    for x in range(0, 4):
        car.append(x)
        stas.append(x)
    for x in range(0, 4):
        car[x] = net.addCar('car%s' % (x), wlans=2, ip='10.0.0.%s/8' % (x + 1), \
        mac='00:00:00:00:00:0%s' % x, mode='b')

    
    eNodeB1 = net.addAccessPoint('eNodeB1', ssid='eNodeB1', dpid='1000000000000000', mode='ac', channel='1', position='80,75,0', range=60)
    eNodeB2 = net.addAccessPoint('eNodeB2', ssid='eNodeB2', dpid='2000000000000000', mode='ac', channel='6', position='180,75,0', range=70)
    rsu1 = net.addAccessPoint('rsu1', ssid='rsu1', dpid='3000000000000000', mode='g', channel='11', position='140,120,0', range=40)
    c1 = net.addController('c1', controller=Controller)
    client = net.addHost ('client')
    switch = net.addSwitch ('switch', dpid='4000000000000000')

    net.plotNode(client, position='125,230,0')
    net.plotNode(switch, position='125,200,0')

    print "*** Configuring wifi nodes"
    net.configureWifiNodes()

    print "*** Creating links"
    net.addLink(eNodeB1, switch)
    net.addLink(eNodeB2, switch)
    net.addLink(rsu1, switch)
    net.addLink(switch, client)

    print "*** Starting network"
    net.build()
    c1.start()
    eNodeB1.start([c1])
    eNodeB2.start([c1])
    rsu1.start([c1])
    switch.start([c1])

    for sw in net.vehicles:
        sw.start([c1])

    i = 1
    j = 2
    for c in car:
        c.cmd('ifconfig %s-wlan0 192.168.0.%s/24 up' % (c, i))
        c.cmd('ifconfig %s-eth0 192.168.1.%s/24 up' % (c, i))
        c.cmd('ip route add 10.0.0.0/8 via 192.168.1.%s' % j)
        i += 2
        j += 2

    i = 1
    j = 2
    for v in net.vehiclesSTA:
        v.cmd('ifconfig %s-eth0 192.168.1.%s/24 up' % (v, j))
        v.cmd('ifconfig %s-mp0 10.0.0.%s/24 up' % (v, i))
        v.cmd('echo 1 > /proc/sys/net/ipv4/ip_forward')
        i += 1
        j += 2

    for v1 in net.vehiclesSTA:
        i = 1
        j = 1
        for v2 in net.vehiclesSTA:
            if v1 != v2:
                v1.cmd('route add -host 192.168.1.%s gw 10.0.0.%s' % (j, i))
            i += 1
            j += 2

    client.cmd('ifconfig client-eth0 200.0.10.2')
    net.vehiclesSTA[0].cmd('ifconfig car0STA-eth0 200.0.10.50')

    car[0].cmd('modprobe bonding mode=3')
    car[0].cmd('ip link add bond0 type bond')
    car[0].cmd('ip link set bond0 address 02:01:02:03:04:08')
    car[0].cmd('ip link set car0-eth0 down')
    car[0].cmd('ip link set car0-eth0 address 00:00:00:00:00:11')
    car[0].cmd('ip link set car0-eth0 master bond0')
    car[0].cmd('ip link set car0-wlan0 down')
    car[0].cmd('ip link set car0-wlan0 address 00:00:00:00:00:15')
    car[0].cmd('ip link set car0-wlan0 master bond0')
    car[0].cmd('ip link set car0-wlan1 down')
    car[0].cmd('ip link set car0-wlan1 address 00:00:00:00:00:13')
    car[0].cmd('ip link set car0-wlan1 master bond0')
    car[0].cmd('ip addr add 200.0.10.100/24 dev bond0')
    car[0].cmd('ip link set bond0 up')

    car[3].cmd('ifconfig car3-wlan0 200.0.10.150')

    client.cmd('ip route add 192.168.1.8 via 200.0.10.150')
    client.cmd('ip route add 10.0.0.1 via 200.0.10.150')

    net.vehiclesSTA[3].cmd('ip route add 200.0.10.2 via 192.168.1.7')
    net.vehiclesSTA[3].cmd('ip route add 200.0.10.100 via 10.0.0.1')
    net.vehiclesSTA[0].cmd('ip route add 200.0.10.2 via 10.0.0.4')

    car[0].cmd('ip route add 10.0.0.4 via 200.0.10.50')
    car[0].cmd('ip route add 192.168.1.7 via 200.0.10.50')
    car[0].cmd('ip route add 200.0.10.2 via 200.0.10.50')
    car[3].cmd('ip route add 200.0.10.100 via 192.168.1.8')

    """plot graph"""
    net.plotGraph(max_x=250, max_y=250)

    net.startGraph()

    # Uncomment and modify the two commands below to stream video using VLC 
    car[0].cmdPrint("vlc -vvv bunnyMob.mp4 --sout '#duplicate{dst=rtp{dst=200.0.10.2,port=5004,mux=ts},dst=display}' :sout-keep &")
    client.cmdPrint("vlc rtp://@200.0.10.2:5004 &")

    car[0].moveNodeTo('95,100,0')
    car[1].moveNodeTo('80,100,0')
    car[2].moveNodeTo('65,100,0')
    car[3].moveNodeTo('50,100,0')

    os.system('ovs-ofctl del-flows switch')

    time.sleep(3)

    apply_experiment(car,client,switch)

    # Uncomment the line below to generate the graph that you implemented
    graphic()

    latency_graph()

    print "***Deleting Files"
    os.system('rm *.apconf')
    os.system('rm *.data')

    # kills all the xterms that have been opened
    os.system('pkill xterm')

    print "*** Running CLI"
    CLI(net)

    print "*** Stopping network"
    net.stop()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    setLogLevel('info')
    try:
        topology()
    except:
        type = sys.exc_info()[0]
        error = sys.exc_info()[1]
        traceback = sys.exc_info()[2]
        print ("Type: %s" % type)
        print ("Error: %s" % error)
        print ("Traceback: %s" % traceback)
        if gnet != None:
            gnet.stop()
        else:
            print "No network was created..."