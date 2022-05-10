import lzma
lzma.LZMAError

from openslides.projector.api import get_active_slide
from openslides.utils import views as utils_views
from openslides.utils.autoupdate import inform_changed_data
from openslides.utils.person import get_person
from openslides.utils.utils import html_strong
from openslides.utils.utils import template
from openslides.utils.utils import template_response
from openslides.utils.utils import update_variable_from_path
from openslides.utils.utils import VERSION

from .forms import (
    CategoryCreateForm, CategoryUpdateForm, SpeakerAddForm, SpeakerDeleteForm,
    RelatedAgendaItemCreateForm, RelatedMotionCreateForm,
    RelatedMediafileAddForm, RelatedMediafileDeleteForm, RelatedProjectorAddForm,
    RelatedProjectorDeleteForm)
from .models import (
    Category, Speaker, CustomSlide, Tag,
    get_all_speakers, get_all_items, get_all_categories, get_all_tags,
    get_all_projectors
