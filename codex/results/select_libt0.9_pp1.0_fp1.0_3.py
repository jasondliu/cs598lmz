import selectedProduct from './selectedProduct'
+import products from './products'
+
+export default combineReducers({
+  products,
+  selectedProduct
+})
+
+// if we would have an extra reducer, we could import it here and add it to combineReducers()

