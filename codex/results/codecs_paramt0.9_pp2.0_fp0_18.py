import codecs
codecs.register_error('strict', codecs.ignore_errors)

# This is just making sure that all the package is present.
# If not, it will leave a list to be pip installed.
def install(package):
    pip3.main(['install', package])

# Package list
# Set this only if you are the dev and you have the latest packages.
installPackages = [
	"beautifulsoup4",
	"six",
	"webencodings",
	"pyasn1",
	"pyasn1-modules",
	"rfc3986",
	"ndg-httpsclient",
    "pyOpenSSL",
    "certifi",
    "chardet",
	"enum34",
	"idna",
	"requests",
	"urllib3"
]

# I'm not good with your...
def not_good_with_your(e):
	print("I'm not good with your", e)
	print("Maybe try again later?")
	sys.exit()

print("Welcome to the story downloader.\nYou
