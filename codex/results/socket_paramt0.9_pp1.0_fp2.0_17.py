import socket
socket.if_indextoname(0xf0e7cc56)
```
9. Locate NetHunter SDK's `manifest.xml` file, and change the `android:value` attribute to the new name.
10. Run `git add` on the `manifest.xml`, and `git commit -m mwifiex_pcie (pcie | sdio | usb)`
