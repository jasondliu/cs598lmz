import weakref

from . import _interfaces, _utils, _vendor
from . import _widgets_core

from . import _widgets_layout

from . import _widgets_selection

from . import _widgets_string

from . import _widgets_table

from . import _widgets_text

from . import _widgets_tree

from . import _widgets_web

from . import _widgets_windows

from ._interfaces import (
    IContextMenuProvider,
    ICommandHandler,
    ICommandProvider,
    IEditor,
    IEditorSession,
    IEditorSessionFactory,
    IEditorSessionFactoryWithArgs,
    IEditorSessionFactoryWithFile,
    IEditorSessionFactoryWithFileAndArgs,
    IEditorSessionFactoryWithFileAndId,
    IEditorSessionFactoryWithId,
    IEditorSessionFactoryWithPath,
    IEditorSessionFactoryWithPathAndArgs,
    IEditorSessionFactoryWithPathAndId,
    IEditorSessionFactoryWithType,
    IEditorSessionFactoryWithTypeAndArgs,
    IEditorSessionFactory
