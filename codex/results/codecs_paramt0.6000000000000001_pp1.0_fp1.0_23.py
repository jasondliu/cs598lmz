import codecs
codecs.register_error('replace_with_space', lambda e: (u' ',e.start + 1))



# --------------------------------------------------
# ---------------  MAIN PROCESSING ----------------
# --------------------------------------------------

def main():
    # --------------------------------------------------
    # ---------------  CONFIGURATION  -----------------
    # --------------------------------------------------

    # 1. Create a config object
    config = Config()

    # 2. Load the configuration
    config.load_config()

    # 3. Get the logger
    logger = config.get_logger()

    # --------------------------------------------------
    # ---------------  DATA LOADING  ------------------
    # --------------------------------------------------

    # 1. Load the data
    logger.info('Loading the data...')
    data_loader = DataLoader(config)

    train_data, dev_data, test_data = data_loader.load_data()

    logger.info('Done.')

    # --------------------------------------------------
    # ---------------  DATA PROCESSING ----------------
    # --------------------------------------------------

    # 1. Create the data preprocessor
    logger.info('Creating the preprocessor...')
    pre
