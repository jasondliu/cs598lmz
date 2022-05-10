import io.reactivex.Observable;
import io.reactivex.ObservableEmitter;
import io.reactivex.ObservableOnSubscribe;
import io.reactivex.Observer;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by xiaoyong.cui
 * on 2016/11/1
 * E-Mail:hellocui@aliyun.com
 */

public class RxJavaTestActivity extends AppCompatActivity {
    private static final String TAG = "RxJavaTestActivity";
    private TextView mTextView;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_rxjavatest);
        mTextView = (TextView) findViewById(R.id.tv_rxjava_test);

