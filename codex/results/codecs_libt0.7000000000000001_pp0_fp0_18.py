import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

# For BioASQ11
# This tells pytorch NOT to compute gradients with respect to model parameters.
# It's important to note that this DOES NOT affect backpropagation, which means
# your network can still learn. It also saves memory, since you don't have to
# store the gradients in memory.

# This was important for me because I was getting OOM (out of memory) errors
# when trying to train the generator and discriminator together on the
# celebrity dataset.

# Comment out the line below if you wish to compute gradients with respect to
# the model parameters.

#torch.set_grad_enabled(False)

# ========================================================
# Setup
# ========================================================

# We can use an image folder dataset the way we have it setup.
# Create the dataset

# Create the dataloader
dataloader = get_loader(transform=transforms.Compose([transforms.Resize(image_size),
                                
