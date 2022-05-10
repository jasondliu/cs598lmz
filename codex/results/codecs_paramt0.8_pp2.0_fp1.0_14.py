import codecs
codecs.register_error("strict", codecs.ignore_errors)

# list of files that we want to include
files = [
    # {name: "filename", overwrite: True/False}
    {"name": "index", "overwrite": True},
    {"name": "index_en", "overwrite": True},
    {"name": "index_de", "overwrite": True},
    {"name": "index_fr", "overwrite": True},
    # {"name": "test", "overwrite": True},
]

# this is to be able to invoke pelican from any directory
this_path = os.path.dirname(os.path.realpath(__file__))

# get the current date and time and format it
now = datetime.datetime.now()
time_str = now.strftime("%Y-%m-%d %H:%M")

# list of tuples [("template string", "output file"), ...]
# the strings in the tuples need to be UTF-8
# the output files need to be Latin-1
# the values in the template strings
