import io.reactivex.Single;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Example 1
        Single.just("Hello")
                .subscribe(new SingleObserver<String>() {
                    @Override
                    public void onSubscribe(Disposable d) {

                    }

                    @Override
                    public void onSuccess(String s) {
                        Log.d("MainActivity", s);
                    }

                    @Override
                    public void onError(Throwable e) {

                    }
                });

        // Example 2
        Single.just("Hello")
                .subscribe(s -> Log.d("MainActivity", s));

        // Example 3
        Single.just("Hello")
                .subscribe(s -> Log.d("MainActivity", s),
                        throwable -> Log.d("MainActivity", throwable.getMessage()));

        // Example 4
        Single.just("Hello")
               
