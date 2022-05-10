import weakref

from . import _cffi_backend
from ._cffi_backend import (
    FFI, CDefError, VerificationError,
    new_enum_type, new_struct_type, new_union_type, new_pointer_type,
    new_function_type, new_array_type, new_void_type, new_primitive_type,
    new_opaque_type, new_enum_type, new_typedef,
    _typeof, sizeof, alignof, buffer,
    addressof, cast, gcp,
    _backendutil,
)
from .cparser import CParser, CConstant, CType, CField, CExternVariable, CEnum, CStructOrUnion, CArrayDeclarator, CArrayType, CTypeDeclarator, CVarDeclaration, CVarDefinition, CEnumerator, CTypeDef, CFuncDecl, CFuncType, CTypeOfExpr, CStructOrUnionDef, CParameter, CIdentifierType, CInitializer, CInitializerList, CMacro, CMacroCall
