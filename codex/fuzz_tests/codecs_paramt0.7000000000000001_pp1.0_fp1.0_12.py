import codecs
codecs.register_error('replace_if_invalid', ReplaceIfInvalid)

import logging

logger = logging.getLogger(__name__)


# TODO: pull this out into config file
# These are the fields that we use in our current workflow
# As we add additional fields, we can add them to this list
# and then change the code to handle them.
REQUIRED_FIELDS = [
    'organization',
    'organization_url',
    'organization_contact',
    'organization_contact_email',
    'beneficiary_name',
    'beneficiary_website',
    'beneficiary_contact',
    'beneficiary_contact_email',
    'beneficiary_contact_phone',
    'project_name',
    'project_url',
    'project_contact',
    'project_contact_email',
    'project_contact_phone',
    'project_address',
    'project_address_city',
    'project_address_state',
    'project_address_zip',
    'project_address_country',
    'project_
