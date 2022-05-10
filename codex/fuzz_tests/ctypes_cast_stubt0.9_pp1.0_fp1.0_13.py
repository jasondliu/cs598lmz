import ctypes
ctypes.cast(None, ctypes.c_void_p)

autograd.__version__

import torchvision
torchvision.__version__

import torchvision.transforms as transforms
import torchvision.models as models
from torchvision.models.resnet import BasicBlock

use_cuda = torch.cuda.is_available()
dtype = torch.cuda.FloatTensor if use_cuda else torch.FloatTensor

def test_network(net, trainloader):

    criterion = nn.MSELoss()
    optimizer = optim.Adam(net.parameters(), lr=0.001)

    dataiter = iter(trainloader)
    images, labels = dataiter.next()

    # Create Variables for the inputs and targets
    inputs = autograd.Variable(images)
    targets = autograd.Variable(images)

    # Clear the gradients from all Variables
    optimizer.zero_grad()

    # Forward pass, then backward pass, then update weights
    output = net.forward(inputs)
    loss = criterion(output, targets
