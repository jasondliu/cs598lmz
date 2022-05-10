import types
types.MethodType = types.MethodType

print('sys.path', sys.path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the Deep-Q-Trading bot')
    parser.add_argument('--config', required=False, default='datasets/config/config.json', help='Configuration file')
    parser.add_argument('--train', required=False, action='store_true', help='Train the bot')
    parser.add_argument('--test', required=False, action='store_true', help='Test the bot')
    parser.add_argument('--actor', required=False, action='store_true', help='Run only actor')
    parser.add_argument('--deep-q-trader', required=False, action='store_true', help='Run only deep-q-trader')
    parser.add_argument('--load-checkpoint', required=False, default=None, help='Whether to load the models from the latest checkpoint. The default is None.')
