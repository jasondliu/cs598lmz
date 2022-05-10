import gc, weakref


class Tree(object):

    def __init__(self, value, left=None, right=None):
        self.left = weakref.ref(left) if left is not None else left
        self.right = weakref.ref(right) if right is not None else right
        self.value = value

    def __repr__(self):
        return (
            'Tree({value!r}, {left!r}, {right!r})'
            .format(
                value=self.value,
                left=self.left().value if self.left else None,
                right=self.right().value if self.right else None,
            )
        )


def make_tree():
    root = Tree('root')
    root.left = Tree('left', Tree('left.left'))
    root.right = Tree('right')
    return root


tree = make_tree()
print(tree)
print(gc.collect())
print(tree)

del tree
print(gc.collect())
print('after deleting root')
print('left: ', tree.
