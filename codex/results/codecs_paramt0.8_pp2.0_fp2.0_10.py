import codecs
codecs.register_error('strict', codecs.ignore_errors)

# If a path is given, set the source as the path if it exists.
# Else, if a source is given, use that as the source.
# Else, use the current directory as the source.
if args.path and os.path.exists(args.path):
    source = args.path
elif args.source:
    source = args.source
else:
    source = os.getcwd()
print("Using {} as the source directory.".format(source))

# If a destination is given, use that as the destination.
# Else, use the current directory as the destination.
if args.destination:
    destination = args.destination
else:
    destination = os.getcwd()
print("Using {} as the destination directory.".format(destination))


# Make sure the destination exists
if not os.path.exists(destination):
    os.makedirs(destination)

# A list of songs that have been successfully added.
successful_songs = []

# A list of songs that could
