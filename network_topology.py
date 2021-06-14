#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI

class MyTopology(Topo):
    """
    A basic topology
    """
    def __init__(self):
        Topo.__init__(self)

        # Set Up Topology Here
        
        # Switches - 1 through 3
        switch1 = self.addSwitch('s1')    ## Adds a Switch
        switch2 = self.addSwitch('s2')    ## Adds a Switch - NEW
        switch3 = self.addSwitch('s3')    ## Adds a Switch - NEW

        # Hosts - 1 through 5
        host1 = self.addHost('h1')       ## Adds a Host
        host2 = self.addHost('h2')       ## Adds a Host - NEW
        host3 = self.addHost('h3')       ## Adds a Host - NEW
        host4 = self.addHost('h4')       ## Adds a Host - NEW
        host5 = self.addHost('h5')       ## Adds a Host - NEW
        

        # Linking switches
        self.addLink(switch1, switch3)
        self.addLink(switch2, switch3)
        #self.addLink(host1, switch)
        
        
        # Linking hosts to switches
        
        #h1,2 to s1
        self.addLink(host1, switch1)
        self.addLink(host2, switch1)
        
        #h3,4 to s2
        self.addLink(host3, switch2)
        self.addLink(host4, switch2)
        
        #h5 to s3
        self.addLink(host5, switch3)
        
        


if __name__ == '__main__':
    """
    If this script is run as an executable (by chmod +x), this is
    what it will do
    """

    topo = MyTopology()            ## Creates the topology
    net = Mininet( topo=topo )        ## Loads the topology
    net.start()                      ## Starts Mininet

    # Commands here will run on the simulated topology
    CLI(net)

    net.stop()                       ## Stops Mininet

    topos = { 'mytopo': ( lambda: MyTopo() ) }
