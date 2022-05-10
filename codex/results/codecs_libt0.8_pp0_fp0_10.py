import codecs
codecs.register(codecs_register)


library_matcher = re.compile(r"^\s*library\s+(?P<identifier>\w+)(\s+is\s+new)?(\s*\(\s*\w+\s*\:\s*[^;\s]+\s*\))?", re.IGNORECASE)
package_matcher = re.compile(r"^\s*package\s+(?P<identifier>\w+)", re.IGNORECASE)
use_matcher = re.compile(r"^\s*use\s+(?P<identifier>[\w.]+)", re.IGNORECASE)
entity_matcher = re.compile(r"^\s*entity\s+(?P<identifier><\w+)", re.IGNORECASE)
arch_matcher = re.compile(r"^\s*architecture\s+(?P<identifier><\w+)", re.IGNORECASE)
component_matcher = re.compile(r"^
