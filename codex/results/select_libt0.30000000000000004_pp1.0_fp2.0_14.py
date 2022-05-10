import select
import socket
import sys
import threading
import time

import pytest

from zeroconf import (
    BadTypeInNameException,
    BadTypeInRecordException,
    BadTypeInServiceInfoException,
    DNSServiceException,
    DNSServiceFlags,
    DNSServiceRef,
    DNSServiceType,
    DNSQuestion,
    DNSRecord,
    DNSRecordType,
    DNSRawRecord,
    DNSRawQuestion,
    DNSRawService,
    DNSRawServiceItem,
    DNSService,
    DNSServiceInterfaceIndex,
    DNSServiceInterfaceIndexAny,
    DNSServiceInterfaceIndexLocalOnly,
    DNSServiceInterfaceIndexUnicast,
    DNSServiceInterfaceIndexP2P,
    DNSServiceInterfaceIndexAnyIncludingP2P,
    DNSServiceInterfaceIndexAWDL,
    DNSServiceInterfaceIndexCellular,
    DNSServiceInterfaceIndexLocalNetwork,
    DNSServiceInterfaceIndexVPN,
    DNSServiceInterfaceIndexWired,
