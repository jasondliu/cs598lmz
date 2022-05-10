import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
f = FUNTYPE(lambda x: x+1)
f(1)

from torch import _C

t = torch.tensor([1], dtype=torch.int64)
t.size()
t.numel()

X = torch.rand(100, 5)
Y = torch.rand(100)

class MyModule(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(5, 10)
        self.linear2 = torch.nn.Linear(10, 1)

    def forward(self, x):
        x = torch.relu(self.linear1(x))
        x = torch.sigmoid(self.linear2(x))
        return x

m = MyModule()
m

opt = torch.optim.Adam(m.parameters(), lr=1e-2)

for i in range(1000):
    y_hat = m(X)

