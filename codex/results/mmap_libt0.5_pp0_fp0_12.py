import mmap
import os

from datetime import datetime
from collections import OrderedDict
from xml.etree import ElementTree
from xml.dom import minidom

from bs4 import BeautifulSoup
from bs4 import UnicodeDammit

from django.core.management.base import BaseCommand
from django.conf import settings

from catalogue.models import Category, Product, ProductImage, ProductCategory
from catalogue.models import ProductAttribute, ProductAttributeValue
from catalogue.models import Option, OptionGroup, ProductOption
from catalogue.models import ProductRecommendation
from catalogue.models import StockRecord
from catalogue.models import Partner, PartnerStockRecord
from catalogue.models import ProductAttributeValue
from catalogue.models import ProductClass, ProductAttribute, AttributeOptionGroup
from catalogue.models import ProductCategory
from catalogue.models import ProductRecommendation

from oscar.core.loading import get_model
from oscar.apps.partner.importers import BaseImporter
from oscar.apps.partner.exceptions import (
    ImporterError, ProductConstraintError, ProductNotFoundError)

from oscar
