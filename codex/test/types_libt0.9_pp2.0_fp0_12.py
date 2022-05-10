import types
types.ModuleType.__eq__ = lambda self, other: self is other


class Model(Params):
    """
    A Model represents abstract base for a transform or an estimator.

    It has the following methods. Subclasses should specify
    what the return types of transform and fit should be.

    - fit
    - transform
    - fitTransform
    - isFitted

    >>> model = Model()
    >>> model.fit([[1]])
    >>> model.transform([[1]])
    """

    def __init__(self):
        super(Model, self).__init__()

    def fit(self, dataset, verbose=True, params=None):
        """
        Fits a model to the input dataset with optional parameters.
        Subclasses should specify the return type.
        """
        self.fitImpl(dataset, params, verbose)
        return self

    def fitImpl(self, dataset, params, verbose):
        """
        Implementation of fit. Subclasses should write the actual
        fitting logic in this method.
        """
