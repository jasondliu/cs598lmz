import types
types.MethodType(SimpleApp, request)

class AppURLopener(urllib.FancyURLopener):
    version = "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0"

urllib._urlopener = AppURLopener()

def main():
    application = web.application(urls, globals())
    application.run()

if __name__ == "__main__":
    main()
