import threading
threading.stack_size(67108864)  # 64MB stack
# Code part of the main function
def main():
    # We create this "assertion" to make sure that we are
    # not trying to start a process which has been initialized
    # If the error appears, that means that there is a bug in the code.
    assert not initialized.value  # check whether the Shared Array has been initialized

    # Setting leaf
    mh.set_leaf(multihead)

    # Get devices id
    ngpus = torch.cuda.device_count()

    torch.cuda.set_device(local_rank)

    # Initalize PRNG
    init_prng(rank)

    # Print info
    print('Rank ', rank, ' has ', ngpus, ' gpus, with local_rank ', local_rank)

    # Set distributed back end
    # We use DDP even for a single node for simplicity.
    # You can always disable this with the --nodistributed option.
    # This is important to handle the distributed case properly in some of your code.
