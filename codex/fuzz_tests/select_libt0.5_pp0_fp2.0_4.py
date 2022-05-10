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
    data = cursor.fetchall()
    logger.info("Got all data")
    return data

def get_data_for_user(cursor, config, user_id):
    """
    Get data for a specific user
    :param cursor: database cursor
    :param config: config file
    :param user_id: user id
    :return: data for user
    """
    logger.info("Getting data for user {}...".format(user_id))
    sql_query = select_data
