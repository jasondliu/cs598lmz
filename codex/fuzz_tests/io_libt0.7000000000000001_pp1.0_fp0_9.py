import io.reactivex.disposables.CompositeDisposable;
+
+public class MainActivity extends AppCompatActivity {
+    private static final String TAG = "MainActivity";
+    private CompositeDisposable compositeDisposable;
+    private CountDownTimer countDownTimer;
+    @Override
+    protected void onCreate(Bundle savedInstanceState) {
+        super.onCreate(savedInstanceState);
+        setContentView(R.layout.activity_main);
+
+        compositeDisposable = new CompositeDisposable();
+
+        Observable<String> observable = Observable.just("one","two","three");
+        Observable<String> observable_two = Observable.just("four","five","six");
+        Observable<String> observable_three = Observable.just("seven","eight","nine");
+        Observable<String> observable_four = Observable.just("ten","eleven","twelve");
+        Observable<String> observable_five = Observable.just("thirteen","fourteen","fifteen");
+
+       
