import io.reactivex.Observable
+import io.reactivex.subjects.PublishSubject
+
+class BookRepoImpl : BookRepo {
+
+    private val favoritesSubject = PublishSubject.create<Pair<Int, Boolean>>()
+
+    override fun getBooks(): LiveData<List<Book>> {
+        val allBooks = Devsbooks.getInstance().allBooks
+        return LiveDataReactiveStreams
+            .fromPublisher(Observable.fromArray(allBooks))
+    }
+
+    override fun hasFavoritedChanged(): LiveData<Pair<Int, Boolean>> {
+        return LiveDataReactiveStreams
+            .fromPublisher(favoritesSubject)
+    }
+
+    override fun favorite(bookId: Int, favorite: Boolean) {
+        favoritesSubject.onNext(Pair(bookId, favorite))
+    }
+
+}

