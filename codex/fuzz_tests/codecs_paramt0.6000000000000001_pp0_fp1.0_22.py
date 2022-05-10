import codecs
codecs.register_error("strict", codecs.ignore_errors)


class Data:
    def __init__(self, db_name, db_user, db_password, db_host, db_port, db_driver_name, db_driver_path, db_type,
                 db_table, db_sql, db_sql_parameters, db_user_defined_query, db_query_columns, db_query_column_widths,
                 db_query_column_titles, db_query_column_types, db_query_column_decimal_places, db_query_column_alignment,
                 db_query_column_date_formats, db_query_column_time_formats, db_query_column_narrative_formats,
                 db_query_column_narrative_custom_formats, db_query_column_narrative_custom_fields,
                 db_query_column_narrative_custom_separators, db_query_column_narrative_custom_display_types,
                 db_query_column_narrative_custom_
