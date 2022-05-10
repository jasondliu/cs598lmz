import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;
import io.reactivex.subjects.PublishSubject;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "MainActivity";
    private static final int REQUEST_CODE = 1001;

    private TextView mTvResult;
    private EditText mEtInput;
    private Button mBtnStart;
    private Button mBtnStop;
    private Button mBtnPost;
    private Button mBtnPublish;
    private Disposable mDisposable;

    private PublishSubject<String> mPublishSubject;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        initView();

        initRxBus();

        initListener();
    }

    private void initView() {
        mE
