import weakref
import logging

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count, CharField, Q, F, Value, ExpressionWrapper
from django.db.models.functions import Concat, Trunc
from django.utils.decorators import classonlymethod
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from sapl.materia.models import MateriaLegislativa, TipoMateriaLegislativa
from sapl.materia.models import TipoProposicao
from sapl.parlamentares.models import Parlamentar, Filiacao
from sapl.sessao.models import SessaoPlenaria, Orador, OrdemDia, ExpedienteMateria
from sapl.sessao.models import ExpedienteSessao, RegistroVotacao
from sapl.utils import (RANGE_ANOS, YES_
