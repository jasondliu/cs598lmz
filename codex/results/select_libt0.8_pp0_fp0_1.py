import selectionSort from './selection';
+
+export default function benchmarkSort(sort, array) {
+  const startDate = new Date();
+  const newArray = sort(array);
+  const endDate = new Date();
+  return {
+    result: newArray,
+    time: endDate - startDate
+  }
+}
+
+export function benchmark(length) {
+  const data = new Array(length).fill(0).map(() => Math.round(Math.random() * length));
+  const { result: insertionResult, time: insertionTime } = benchmarkSort(insertionSort, data);
+  const { result: selectionResult, time: selectionTime } = benchmarkSort(selectionSort, data);
+  return {
+    result: {
+      insertionSort: [...insertionResult],
+      selectionSort: [...selectionResult]
+    },
+    time: {
+      selectionSort: selectionTime,
+      insertionSort: insertionTime
+    }
+  }
+}
+
+// benchmark(10000);

