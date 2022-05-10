import types
types.ModuleType( 'trini' )

#----------------------------------------------------------------------------------------------------------------------------------
# dependencies

import db.inflector
import db.translator
import db.query
import db.sqltypes
import db.result
import db.runtime

#----------------------------------------------------------------------------------------------------------------------------------
# public types

@db.sqltypes.SQLType.delegated
class Enum( object ):

    def __init__( self, enum_type, enum_name, enum_symbols ):
        self.enum_type = enum_type
        self.enum_name = enum_name
        self.enum_symbols = enum_symbols

    def __str__( self ):
        return '"{}"'.format( self.enum_name )

    def as_text( self, db_name ):
        if db_name in ('postgres', 'postgresql'):
            return self.enum_name
        elif db_name == 'mssql':
            return self.enum_name
        elif db_name == 'mysql':
            return 'enum ' + self.enum_name
