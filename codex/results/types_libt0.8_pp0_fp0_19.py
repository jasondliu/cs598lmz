import types
types.ClassType = type

from cStringIO import StringIO

class MyMock(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class Test_example(unittest.TestCase):
    
    
    
    
    
    
    
    
    
    
    @mock.patch('__builtin__.open')
    def test_example(self, mock_open):
        mock_open('/etc/passwd').readline.return_value = \
            'root:x:0:0:root:/root:/bin/bash\n'
        
        mock_file = mock.MagicMock(spec=file)
        mock_file.writelines.return_value = None
        
        mock_open.return_value = mock_file
        
        example.example()
        
        mock_open.assert_called_with('/etc/passwd')
        
        mock_file.write.assert_called_with('root')
        
        expected = [
            mock.
