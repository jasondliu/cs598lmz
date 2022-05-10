import socket
socket.if_indextoname(1)

import boto.ec2
from boto.ec2.connection import EC2Connection
region = boto.ec2.get_region('us-west-2')
conn = boto.connect_ec2(region=region)

reservation = conn.get_all_instances()[0]
instances = reservation.instances

instances[0].private_dns_name

reservation.instances[0].private_dns_name

instances[0].groups[0].name

instances[0].key_name

instances[0].security_groups[0].name

reservation.instances[0].private_ip_address

reservation.instances[0].public_dns_name

instances[0].launch_time

instances[0].image_id

instances[0].instance_type

instances[0].state

instances[0].state_code

instances[0].get_attribute('userData')

instances[0].tags

