import codecs
codecs.register_error('strict', codecs.ignore_errors)

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.db import transaction
from django.db.models import Q
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from ...models import (
    Category,
    Product,
    ProductImage,
    ProductVariant,
    ProductAttribute,
    ProductAttributeValue,
    Stock,
    AttributeChoiceValue,
    Attribute,
    AttributeChoice,
    ProductClass,
    ProductType,
    ProductTypeAttribute,
    ProductTypeAttributeDefault,
    ProductTypeVariant,
    ProductTypeVariantAttribute,
    ProductTypeVariantAttributeValue,
    ProductTypeVariantImage,
    ProductTypeVariantStock,
    ProductTypeVariantStockLocation,
    ProductTypeVariantStockWarehouse,
    ProductTypeVariantStockWarehouseLocation,
    ProductTypeVariantStockWarehouseLocationStock,
    ProductTypeVariantStockWarehouseLocation
