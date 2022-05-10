import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

from django.views.generic import View
from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
import json
from django.db import connections

from datetime import datetime
import time
from .models import (
    Periodo,
    Contratos,
    ContratosEstadosDetalle,
    ContratosPagoDetalle,
    ContratosPagoPendiente,
    ContratosClaves,
    ContratosClavesDetalle,
    ContratosPagoPendienteClaves,
    ContratosRetencion,
    ContratosRetencionDetalle,
    ContratosPagoPendienteRetencion,
    ContratosObrasDetalle,
    ContratosPagoPendienteObras,
    ContratosTipos,
    ContratosTiposDetalle,
    Cont
