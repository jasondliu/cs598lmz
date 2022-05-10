import io.reactivex.Observable;
import io.reactivex.ObservableEmitter;
import io.reactivex.ObservableOnSubscribe;
import io.reactivex.Observer;
import io.reactivex.annotations.NonNull;
import io.reactivex.disposables.Disposable;

/**
 * Created by yangc on 2017/9/13.
 * E-Mail:yangchaojiang@outlook.com
 * Deprecated: rxjava2.0 基础类
 */

public class RxJava2BaseActivity extends AppCompatActivity {
    private static final String TAG = "RxJava2BaseActivity";
    private TextView tv;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_rxjava2_base);
        tv = (TextView) findViewById(R.id.tv);
        findViewById(R.id.btn_1).setOnClickListener
