import lzma
lzma.LZMAError

# check for git
import subprocess
try:
    subprocess.check_call(['git', '--version'], stdout=subprocess.DEVNULL)
except (OSError, subprocess.CalledProcessError):
    print('Warning: git not found, some functionality will be disabled')

# check for OpenSSL
try:
    subprocess.check_call(['openssl', 'version'], stdout=subprocess.DEVNULL)
except OSError:
    print('Warning: openssl not found, some functionality will be disabled')
except subprocess.CalledProcessError:
    print('Warning: openssl not found, some functionality will be disabled')

# check for OpenSSL 1.1.1
try:
    subprocess.check_call(['openssl', 'version', '-v'], stdout=subprocess.DEVNULL)
except OSError:
    pass
except subprocess.CalledProcessError:
    pass
else:
    print('Warning: openssl found in version 1.1.1')

# check for
