import select_data
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_all_data(cursor, config):
    """
    Get all data from the database
    :param cursor: database cursor
    :param config: config file
    :return: all data
    """
    logger.info("Getting all data...")
    sql_query = select_data.SELECT_ALL_DATA.format(config.get("main", "table_name"))
    cursor.execute(sql_query)
