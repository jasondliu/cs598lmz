from lzma import LZMADecompressor
LZMADecompressor().decompress(model_serialized[9:2289])
</code>
and it returns <code>b'MZ\x90\x00\x03\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00!\x00'</code> because it does not have the lzma header.
I am sure that my trained model is saved into the <code>model_serialized</code> variables, because if I load in the python interpreter via <code>torch.load('reid_model_69.pth')</code>, everything works fine, but I cannot use this method in production, while I will deploy my docker container on the Production server.
Please help. Thanks!


A:

I'd recommend to use the <code>torch.jit.trace</code> method instead of <code>torch.save</code>. The <code>torch.jit.trace</code> method also saves the model, but it also generates a <code>script</code>- and <code>graph</code-
