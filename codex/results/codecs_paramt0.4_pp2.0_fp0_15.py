import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Global variables
#
# Use the following variables in your code:
#
# logger:   Logging object. Use logger.info("..."), logger.warning("..."), logger.exception("...")
#           and logger.debug("...") to write to the log file and console, as appropriate.
#
# config:   A ConfigParser object. Use config.get("section", "key") to read values from the
#           configuration file.
#
# args:     A Namespace object. Use args.var to read command-line arguments.
#
# db:       A MySQL database connection object. Use db.cursor() to create a cursor, then
#           cursor.execute(...) to execute SQL, and cursor.fetchone() to retrieve a row,
#           and so on. See the MySQLdb documentation.
#
# cur:      The database cursor most recently created by db.cursor().
#
# _:        A function that does nothing. Use this as a placeholder for callback functions,
#           when you aren't using them.
#

logger
