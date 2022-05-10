import select from './select';
+
+const reducer = combineReducers({
+  hospitals: hospitalsReducer,
+  select: select,
+});
+
+const store = createStore(reducer, applyMiddleware(thunk));
+
+ReactDOM.render(
+  <Provider store={store}>
+    <App />
+  </Provider>,
+  document.getElementById('root')
+);

