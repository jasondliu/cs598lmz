import types
types.ClassType = type

from zope.interface import implements

from AccessControl import ClassSecurityInfo

from Products.CMFCore.permissions import View
from Products.CMFCore.permissions import ModifyPortalContent

from Products.Archetypes.atapi import *
from Products.ATContentTypes.content.file import ATFileSchema
from Products.ATContentTypes.content.base import registerATCT
from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from Products.PFGExtendedMailAdapter.interfaces import IPFGExtendedMailAdapter

from Products.CMFCore.utils import getToolByName
pfgextendedmailadapter_schema = ATFileSchema.copy() + Schema((
    StringField('title',
                required=1,
                accessor='Title',
                searchable=1,
                mutator='setTitle',
                widget=StringWidget(
                    description="Title of the mail adapter",
                    description_msgid='help_title_mailadapter',
                    label='Title',
                    label_msgid
