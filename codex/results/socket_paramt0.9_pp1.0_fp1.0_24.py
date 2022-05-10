import socket
socket.if_indextoname(1)

#    for mib in SNMP_MODULES:
#        netSnmpModuleObject = prefixed_MibScalarInstance(
#                subid=(0,),
#                oidstr='NET-SNMP-%s-MIB::netSnmpModule%s.0' % (
#                    mib.upper(), mib.capitalize()))

netSnmpModuleCount = prefixed_MibScalar((1, 3, 6, 1, 4, 1, 8072, 2, 1, 1))
netSnmpModuleName = prefixed_MibScalar((1, 3, 6, 1, 4, 1, 8072, 2, 1, 1))

snmpNotifyFilterStorageType = MibTableColumn((1, 3, 6, 1, 6, 3, 21, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
snmpTargetAddrTagList = MibTableColumn((1, 3, 6, 1, 6, 3, 12, 1, 2, 3, 2), OctetString()).
