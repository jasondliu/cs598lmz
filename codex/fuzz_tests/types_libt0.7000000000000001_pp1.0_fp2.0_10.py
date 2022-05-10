import types
types.ModuleType('__builtin__').__dict__['__import__'] = my_import

import test_import

print 'test_import.x =', test_import.x
</code>
The output is:
<code>Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden __import__
Overridden
