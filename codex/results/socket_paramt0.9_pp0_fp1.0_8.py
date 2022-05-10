import socket
socket.if_indextoname(socket.if_nametoindex('en0'))
 */

/*
 //
 // WithCoreFoundation
 //
 let en0 = CFStringCreateWithCString(nil, "en0", CFStringBuiltInEncodings.UTF8.rawValue)
 if en0 != nil {
    var addr: Unmanaged<CFSocketAddress>?
    var iface: Unmanaged<CFSocketNativeHandle>?
    
    if CFSocketCreate(kCFAllocatorDefault, PF_INET, SOCK_DGRAM, IPPROTO_IP, kCFSocketAutomaticallyReenableReadCallBack, nil, &iface) != kCFSocketSuccess {
        return nil
    }
    
    if CFSocketCopyAddress(iface!.takeRetainedValue()) == nil {
        if CFSocketCreate(kCFAllocatorDefault, PF_INET, SOCK_DGRAM, IPPROTO_IP, 0, nil, &iface) != kCFSocketSuccess {
            return nil
        }
    }
    addr = CFSocketCopyAddress(iface
