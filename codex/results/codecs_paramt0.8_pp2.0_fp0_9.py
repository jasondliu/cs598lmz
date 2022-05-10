import codecs
codecs.register_error('strict_replace', codecs.lookup_error('replace'))
import urllib.request
from bs4 import BeautifulSoup
from src.models.schemas.provider import Provider
from src.common.database import Database
from src.models.schemas.item import Item
from src.models.schemas.item_category import ItemCategory
from src.models.schemas.item_types import ItemTypes
from src.models.schemas.item_vendors import ItemVendors
from src.models.schemas.item_tags import ItemTags
from src.models.schemas.item_providers import ItemProviders
from src.models.schemas.provider import Provider
from src.models.schemas.tags import Tag
from src.common.constants import *
import datetime

#############################
# Functions                  #
#############################
def return_tag_id(tag_name, tag_label, tag_provider_id):
    tag_data = Tag.get_by_name(tag_name)
    if
