import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

# import MySQLdb
# MySQLdb.converters.encoders[128] = MySQLdb.converters.encoders[str]
# MySQLdb.converters.conversions[128] = MySQLdb.converters.conversions[str]

# import MySQLdb.constants
# import MySQLdb.converters
# import MySQLdb.connections

# MySQLdb.connections.encoders[128] = MySQLdb.connections.encoders[str]
# MySQLdb.connections.converters[128] = MySQLdb.connections.converters[str]

# MySQLdb.constants.FIELD_TYPE.VAR_STRING = MySQLdb.constants.FIELD_TYPE.STRING
# MySQLdb.constants.FIELD_TYPE.STRING = MySQLdb.constants.FIELD_TYPE.STRING

# MySQL
