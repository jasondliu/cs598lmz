import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Base(object):
    """
    Base class for all models.
    """
    
    def __init__(self, *args, **kwargs):
        """
        Initialize the model.
        """
        self.args = args
        self.kwargs = kwargs
    
    def __repr__(self):
        """
        Return a string representation of the model.
        """
        return '%s(%s)' % (self.__class__.__name__, ', '.join(['%s=%s' % (k, v) for k, v in self.__dict__.items()]))
    
    def __str__(self):
        """
        Return a string representation of the model.
        """
        return self.__class__.__name__
    
    def __unicode__(self):
        """
        Return a string representation of the model.
        """
        return unicode(self.__str__())
    
    def __eq__(self, other):
       
