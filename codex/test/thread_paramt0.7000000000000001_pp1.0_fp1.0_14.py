import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\r' + ' ' * 100 + '\r')).start()

# Create models
encoder = Encoder()
decoder = Decoder(output_size=output_size, hidden_size=hidden_size)

# Move models to GPU
if USE_CUDA:
    encoder.cuda()
    decoder.cuda()

# Initialize optimizers and criterion
learning_rate = 0.0001
encoder_optimizer = torch.optim.Adam(encoder.parameters(), lr=learning_rate)
decoder_optimizer = torch.optim.Adam(decoder.parameters(), lr=learning_rate)
criterion = nn.NLLLoss()

# Keep track of time elapsed and running averages
start = time.time()
plot_losses = []
print_loss_total = 0 # Reset every print_every
plot_loss_total = 0 # Reset every plot_every


# Begin!
