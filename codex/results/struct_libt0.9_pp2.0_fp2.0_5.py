import _struct from './struct.js';
+
+const userList = immutable.fromJS({});
+
+const user = (state = userList, action) => {
+  switch (action.type) {
+    case 'SET_USER':
+      return state.setIn(['user', action.key], action.value);
+    case 'SET_BEANS':
+      return state.setIn(['user', 'beans'], action.value);
+    case 'HAS_LOGIN':
+      return state.set('isLogin', action.value);
+    default:
+      return state;
+  }
+};
+
+export default user;

