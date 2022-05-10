import types
types.ModuleType('pygments')
import pygments

import pygments.lexers
import pygments.formatters

class CodeHighlighter(object):
    def __init__(self, style, language):
        self._style = style
        self._language = language

    def highlight(self, code):
        lexer = pygments.lexers.get_lexer_by_name(self._language)
        formatter = pygments.formatters.HtmlFormatter(style=self._style)
        return pygments.highlight(code, lexer, formatter)

class CodeBlock(blocks.StructBlock):
    language = blocks.ChoiceBlock(choices=[
        ('python', 'Python'),
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('js', 'JavaScript'),
        ('bash', 'Bash'),
    ])
    code = blocks.TextBlock()

    class Meta:
        icon = 'code'
