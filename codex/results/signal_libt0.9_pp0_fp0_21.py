import signal
signal.signal(signal.SIGINT, signal_handler)
# Set up device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
device

# Set up random seed for reproducible training
random.seed(2050)
np.random.seed(2050)
torch.manual_seed(2050)
torch.cuda.manual_seed_all(2050)
# Read training and validation data
train_data = pd.read_csv('../../train_data/train_data_v6_countenc.csv', dtype={'fullVisitorId': str})
test_data = pd.read_csv('../../train_data/test_data_v6_countenc.csv', dtype={'fullVisitorId': str})

# Extract target column
train_y = train_data[['totals.transactionRevenue']].fillna(0)
train_id = train_data['fullVisitorId']
test_id = test_data['fullVisitorId']
# Drop
