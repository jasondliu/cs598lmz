import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
import json
import ns.core

ns.core.LogComponentEnable("UdpEchoClientApplication", ns.core.LOG_LEVEL_INFO)
ns.core.LogComponentEnable("UdpEchoServerApplication", ns.core.LOG_LEVEL_INFO)

n = 1

cmd = ns.network.CommandLine()
cmd.AddValue("n","Number of echos",n)

cmd.Parse(sys.argv)

n = int(n)

print("creating " + str(n) + " echos.")

nodes = ns.network.NodeContainer()
nodes.Create(2)

pointToPoint = ns.point_to_point.PointToPointHelper()
pointToPoint.SetDeviceAttribute("DataRate",ns.network.StringValue("5Mbps"))
pointToPoint.SetChannelAttribute("Delay",ns.network.StringValue("2ms"))

devices = pointToPoint.Install(nodes
