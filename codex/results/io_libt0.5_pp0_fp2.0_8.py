import io.reactivex.disposables.Disposable;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //观察者
        Observer<String> observer = new Observer<String>() {
            @Override
            public void onSubscribe(Disposable d) {
                Log.d("TAG", "onSubscribe");
            }

            @Override
            public void onNext(String s) {
                Log.d("TAG", "onNext: " + s);
            }

            @Override
            public void onError(Throwable e) {
                Log.d("TAG", "onError");
            }

            @Override
            public void onComplete() {
                Log.d("TAG", "onComplete");
            }
        };

        //被观察者
        Observable<String> observable = Observable.create(new ObservableOnSubscribe<String>() {
