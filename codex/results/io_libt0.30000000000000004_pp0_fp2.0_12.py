import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "MainActivity";

    private Disposable disposable;
    private Disposable disposable2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Observable
        Observable<String> animalsObservable = getAnimalsObservable();

        // Observer
        Observer<String> animalsObserver = getAnimalsObserver();

        // Observer subscribing to Observable
        animalsObservable
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribeWith(animalsObserver);

        // Observer subscribing to Observable
        disposable = animalsObservable
               
