import gc, weakref

from .control_panel.utils import (check_for_similarity,
                                  get_error_message_from_validation_error)
from .control_panel.site_registry import (site_registry,
                                          AlreadyRegistered,
                                          NotRegistered)
from .widgets import (ControlPanel,
                      ControlPanelForm,
                      ControlPanelFormField)


def set_app_models(app_models):

    site_registry.app_models = app_models
    site_registry.fields = {}
    site_registry.editable_fields = {}
    site_registry.field_types = {}
    site_registry.form_fields = {}
    site_registry.form_classes = {}
    site_registry.model_form_classes = {}
    site_registry.field_options = {}
    site_registry.all_models = set()


def get_app_models():

    return site_registry.app_models


def register(model):

    if model in site_registry.app_models:
