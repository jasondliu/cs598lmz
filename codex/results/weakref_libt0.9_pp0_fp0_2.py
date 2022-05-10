import weakref

from minidb.core.base.exceptions import ForeignKeyException
from minidb.core.base.types import Field, FieldType
from minidb.utils.validators_generators import (
    generate_related_validator,
    generate_size_validator,
    generate_type_validator,
    generate_unique_validator,
)


class RelatedTo(Field):
    def __new__(cls, table_name, schema, is_null):
        new_field = super(RelatedTo, cls).__new__(cls, table_name, schema, is_null)

        size = len(new_field.base_table)
        new_field.size = size
        new_field.type = FieldType.Related
        new_field.validator_list.append(generate_type_validator(size))
        new_field.validator_list.append(generate_related_validator(new_field, weakref.ref(new_field)))
        new_field.validator_list.append(generate_size_
