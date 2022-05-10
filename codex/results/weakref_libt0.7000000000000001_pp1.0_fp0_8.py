import weakref

manage_addMESSAGEFORM_html = PageTemplateFile('zpt/add', globals())

def manage_addMESSAGEFORM(dispatcher, id, title='', RESPONSE=None,
                          method='POST', url=None, description='',
                          topic='', lang='en'):
    """Add an MESSAGEFORM to a Plone site."""

    id = id.replace(' ', '_')

    if not url:
        url = '%s/%s' % (dispatcher.DestinationURL(), id)

    ob = MESSAGEFORM(id, title, method, url, description, topic, lang)

    dispatcher._setObject(id, ob)

    if RESPONSE is not None:
        RESPONSE.redirect('%s/manage_main' % dispatcher.DestinationURL())

class MESSAGEFORM(Folder, Implicit):
    """A form that sends a message to an e-mail address."""

    meta_type = 'MESSAGEFORM'
    security = ClassSecurity
