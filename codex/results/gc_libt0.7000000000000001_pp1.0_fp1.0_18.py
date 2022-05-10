import gc, weakref

import ic.utils.util as util

from . import icwidget

_ = wx.GetTranslation

#   Тип компонента
ic_class_type = icDefInf._icUserType

#   Имя класса
ic_class_name = 'icRadioButton'

#   Описание стилей компонента
ic_class_styles = {'RADIO_GROUP': wx.RB_GROUP}

#   Спецификация на ресурсное описание класса
ic_class_spc = {'type': 'RadioButton',
                'name': 'default',
                'child': [],
                'activate': True,
                'init_expr': None,
                '_uuid': None,

                'label
