import signal
signal.signal(signal.SIGINT, handler)

# random seed
seed = int(time.time())
np.random.seed(seed)
torch.manual_seed(seed)
if cuda:
    torch.cuda.manual_seed(seed)

# model
model = MNIST_CNN().cuda() if cuda else MNIST_CNN()
#model = LeNet().cuda() if cuda else LeNet()

# setup training
lr = 0.1 #initial learning rate
weight_decay = 3e-4 #weight decay
momentum = 0.9
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr, momentum=momentum, weight_decay=weight_decay)

## setup tensorboard
#writer = SummaryWriter()
#train_batch_log_interval = 100
#eval_frequency = 1

## load from checkpoint
#if args.resume:
#    if os.path.isfile(args.resume):
#       
