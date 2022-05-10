import socket
socket.if_indextoname(2)

'''

from .models import Ipv4Address
from .models import Ipv6Address
from .models import MacAddress
from .models import Interface

from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from django.core.exceptions import ObjectDoesNotExist
from netaddr import IPNetwork, IPAddress
import netifaces


class Command(BaseCommand):
    help = 'Pretty print the routing table.'

    def handle(self, *args, **options):
        for interface in netifaces.interfaces():
            try:
                iface = Interface.objects.get(name=interface)
            except ObjectDoesNotExist:
                iface = Interface(name=interface)
                iface.save()
            try:
                iface.ipv4_address.add(
                    Ipv4Address.objects.get(
                        address=netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']))
            except KeyError:
                pass
