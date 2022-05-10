import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import base


class Markup(base.Markup):
    def __init__(self, text, markup):
        super(Markup, self).__init__(text, markup)
        self.title = text
        self.entry = markup.h.entry(
            markup.h.id(self.link),
            markup.h.link(rel='alternate', type='text/html', href=self.link),
            markup.h.updated(self.updated.isoformat()),
            markup.h.title(text),
            markup.h.author(markup.h.name(self.author)),
            markup.h.summary(text, type='html'),
        )
        self.entry.append(markup.h.content(self.content, type='html'))

    @property
    def content(self):
        return self.markup.render(self.text)

    @property
    def link(self):
        return '/%s.html' % self.filename

    @property
    def
