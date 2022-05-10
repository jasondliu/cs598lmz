import select from 'select-dom'
+import classNames from 'classnames'
+
+/**
+ * Handler for performing various tasks on comments.
+ *
+ * @author  n461306
+ * @param   {Selector}  button  Button element to be attached to.
+ * @param   {String}    action  Action to be performed. Options are:
+ *                                * delete - Deletes thread
+ *                                * quote - Creates new comment quoting thread
+ * @version 1.0
+ */
+export default class CommentsHandler {
+    constructor (button, action) {
+        this.action = action
+        this.$commentsForm = select('.js-issue-sidebar-form')
+        this.$textArea = select('.js-comment-field')
+
+        this.$button = select(button)
+        this.$button.addEventListener('click', this.execute.bind(this))
+    }
+
+    /**
+     * Performs action on comments.
+     * 
+     * @version 1.0
+    
