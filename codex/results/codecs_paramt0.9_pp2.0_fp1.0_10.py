import codecs
codecs.register_error(
    "strict", codecs.strict_errors,
    # Allow other errors to be raised, like
    #  `UnicodeEncodeError` and `UnicodeDecodeError`
    # (their messages should be more helpful).
    onerror=codecs.replace_errors
)

# TemplateLoader gets this from sys.path automatically
# We want to force it to search the directory where the script is.
# This way we can compile the template and use it even if the
# script is called from elsewhere.
# (see also: https://github.com/mitsuhiko/jinja2/issues/164
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "info.sqlite")

current_dir = os.path.dirname(__file__)
current_dir = os.path.abspath(current_dir)
compiled_template_dir = os.path.join(current_dir, "templates_c")

def generate_sql_model(template_file,
                       tree_file,
