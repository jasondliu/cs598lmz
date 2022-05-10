import codecs
# Test codecs.register_error
-	register_error('strict', codecs.strict_errors)
+	codecs.register_error('strict', codecs.strict_errors)
--- a/Lib/test/test_importlib/test_abc.py
+++ b/Lib/test/test_importlib/test_abc.py
@@ -1,4 +1,4 @@
-# Copyright (C) 2011-2012 Petri Lehtinen <petri@digip.org>
+# Copyright (C) 2011-2013 Petri Lehtinen <petri@digip.org>
 #
 # This program is free software; you can redistribute it and/or modify it under
 # the terms of the GNU General Public License as published by the Free Software
