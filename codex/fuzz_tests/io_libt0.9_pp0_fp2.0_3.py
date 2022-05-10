import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;

/**
 * Description:
 * User: xjp
 * Date: 2018/7/31
 * Time: 12:15
 */

public class Main3Activity extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

    }

    private void test() {
        Observable<Integer> observable = Observable.create(new ObservableOnSubscribe<Integer>() {
            @Override
            public void subscribe(ObservableEmitter<Integer> e) throws Exception {
                for (int i = 0; i < 5; i++) {
                    e.onNext(i);
                }
                Thread.sleep(1000);
                e.onComplete();
            }
        });

        Disposable subscribe = observable
                .subscribeOn(Schedulers.io())
                .
