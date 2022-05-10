import codecs
codecs.register_error("strict", codecs.ignore_errors)

from jinja2 import Environment, FileSystemLoader

from . import config
from . import util


def render_template(template_name, context, template_dir=config.TEMPLATE_DIR):
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_name)
    return template.render(context)


def write_markdown_file(output_dir, file_name, markdown):
    output_file = os.path.join(output_dir, file_name)
    util.ensure_dir(output_file)
    with codecs.open(output_file, "w", "utf8") as f:
        f.write(markdown)


def write_html_file(output_dir, file_name, html):
    output_file = os.path.join(output_dir, file_name)
    util.ensure_dir(output_file)
    with codecs.open(output_file, "w", "utf8")
