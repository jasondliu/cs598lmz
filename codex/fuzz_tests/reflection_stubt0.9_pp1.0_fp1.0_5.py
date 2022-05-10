fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.send   # BOOM!
fn.__code__()
```

You can find this function inside the `test_utils` module.

Obviously, this crash happens when you try to send something to an exhausted iterator. To avoid this crash, we always create closed iterators, instead. This is accomplished in the `general_utils` module by overriding the behavior of the `SM_Linker` class.

The `NN_Linker` class was created to give the possibility to create open iterators, too. But it is only used in one case; the `create_network()` function, which you see in the `nn` module of the `tfsnippet`.

As you see in the code below, an iterator is created to train the generator and the discriminator. This iterator is not satisfied!

```python
# _internal/nn.py
train_g = create_optimizer(train_conf.get('g'), g.parameters())
train_d = create_optimizer(train_conf.get('d'), d.parameters())
train_steps = train_conf.get('g_steps',
