import signal
signal.signal(signal.SIGINT, signal.default_int_handler)

# Create a new instance of the API class
api = infoblox.Infoblox(
    "infoblox.example.com",
    username="admin",
    password="infoblox",
    ssl_verify=False,
    http_request_timeout=10,
)

# Get list of all DHCP networks
networks = api.network.get(network_type="dhcp")

# Retrieve the first network
network = networks[0]

# Get list of all DHCP subnets in the network
subnets = network.get_subnets()

# Retrieve the first subnet
subnet = subnets[0]

# Get all DHCP reservations in the subnet
reservations = subnet.get_reservations()

# Get a specific reservation
reservation = subnet.get_reservation(ip="192.168.0.100")

# Create a DHCP reservation
subnet.create_reservation(
    ip="192.168.0.100",
   
