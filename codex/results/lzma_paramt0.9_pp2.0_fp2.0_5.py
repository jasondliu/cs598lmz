from lzma import LZMADecompressor
LZMADecompressor()
```
It will give you the following error:
```
ERROR:root:Invalid Python environment: Python is too old (requires version 3.0 or later) or extension modules are not built correctly
```
If you've followed the instructions correctly you should be able to import (as above) after calling `source scripts/activate`

### Setting up SSL

Currently there seems to be a problem with passenger complaining about a missing cipher list and when there is no
cipher list specified. To get around this SunGard has agreed to install a valid cipher list and otherwise ignore it.

## IIS Instructions

_These instructions have been tested on TLS 1.0, 1.1, 1.2 and SSL 3.0. They should be
the same for any other version of IIS. These instructions use version 3.5 of the .NET Framework, which should work
on IIS5 and later._

### Secure Communication

1. Open IIS Manager.
2. Under IIS select "Application Pools".
3. Right-click on the "AiTools" app pool and select "Advanced Settings".
4. Select the "General" group on
