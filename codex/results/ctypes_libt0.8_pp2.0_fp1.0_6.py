import ctypes
ctypes.cdll.LoadLibrary('libquad.so')
# ctypes.cdll.LoadLibrary('libquad_av.so')

args = parser.parse_args()

if args.device:
    os.environ["CUDA_VISIBLE_DEVICES"] = args.device

# if 'resume' in args and args.resume is not None:
#     model_path = args.resume
# else:
#     model_path = args.model

model_path = args.model

cfg = yaml.load(open(args.cfg))

# random seed
np.random.seed(cfg['random_seed'])
torch.manual_seed(cfg['random_seed'])
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(cfg['random_seed'])

kwargs = {}
if torch.cuda.is_available():
    kwargs = {'num_workers': 1, 'pin_memory': True}


if cfg['dataset_name'] =='ImageNet
