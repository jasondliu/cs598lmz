import io.reactivex.Observable;
import io.reactivex.ObservableEmitter;
import io.reactivex.ObservableOnSubscribe;
import io.reactivex.Observer;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by zhangyunfei on 16/9/18.
 */
public class RxJavaTestActivity extends Activity {
    private TextView mTextView;
    private Button mButton;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_rxjava_test);
        mTextView = (TextView) findViewById(R.id.tv_rxjava_test);
        mButton = (Button) findViewById(R.id.btn_rxjava_test);
        mButton.setOnClick
