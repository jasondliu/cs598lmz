import threading
threading.stack_size(67108864)

@pytest.mark.parametrize(
    "block_size,batch",
    [(128, 256),
     (1024, 128)
     ]
)
def test_relayout_backward(block_size, batch):
    context.set_context(mode=context.GRAPH_MODE, device_target="GPU", save_graphs=True)
    input_shape = (batch, block_size, block_size, 3)
    output_shape = (block_size, batch, 3, block_size)
    input_me = Tensor(np.ones(input_shape), dtype=ms.float32)
    output_me = Tensor(np.ones(output_shape), dtype=ms.float32)

    input_pytorch = np.ones(input_shape)
    output_pytorch = np.ones(output_shape)
    grad_pytorch = np.ones(input_shape)

