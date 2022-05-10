import codecs
codecs.register_error('surrogate_escape', codecs.surrogateescape_error)

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

# Set up environment
env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

# Get the list of files
files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.html')]

# Read the template
template = env.get_template('template.html')

# Render the template
for f in files:
    logging.info('Processing %s', f)

    # Read the file
    with codecs.open(f, 'r', encoding='utf-8', errors='surrogate_escape') as file:
        content = file.read()

    # Render the template
    rendered = template.render(content=content)

    # Write the file
