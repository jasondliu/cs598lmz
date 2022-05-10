import mmap
+
+from . import model
+from . import utils
+from . import config
+from . import logging
+
+
+def get_model(model_name):
+    """Get model by name."""
+    return model.get_model(model_name,
+                           config.MODEL_PATH,
+                           config.MODEL_ARCHIVE_MAP[model_name])
+
+
+def get_model_for_task(task_name):
+    """Get the default model for a task."""
+    return get_model(config.TASK_MODEL_MAP[task_name])
+
+
+def build_task(task_name):
+    """Build task by name."""
+    return utils.get_task(task_name,
+                          config.TASK_PATH,
+                          config.TASK_MODEL_MAP[task_name])
+
+
+def load_data(filename):
+    """Load data into memory from a file."""
+    with open(filename,
