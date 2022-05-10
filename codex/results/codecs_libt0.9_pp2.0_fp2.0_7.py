import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)


class data_parser:

    """
    Example Config:
        {
            "collection_name": "flow_data",
            "db_name": "sensordb",
            "input_path": "/IdealCloud/data/flow_data.csv",
            "output_path": "/IdealCloud/data/processed_flow_data.csv",
            "process": [
                {
                    "type": "filter",
                    "filter": "dates",
                    "start": {
                        "year": [2017]
                    }
                }
            ]
        }
    """

    ########################################################################
    ############################# INITIALIZATION ###########################
    ########################################################################

    @staticmethod
    def get_config(config_file):
        """
        This function load the configuration file

        string -> dictionary
        """
        with open(config_file) as json_file:
            config = json.load(json
