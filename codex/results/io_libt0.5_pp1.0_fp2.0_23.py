import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;

/**
 * @author: liyabin
 * @description:
 * @projectName: AndroidDemo
 * @date: 2016-11-17
 * @time: 18:01
 */
public class RxJavaActivity extends AppCompatActivity implements View.OnClickListener
{
    private static final String TAG = "RxJavaActivity";
    private ActivityRxJavaBinding mBinding;
    private Disposable mDisposable;
    private Observable<Integer> mObservable;
    private Observer<Integer> mObserver;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        mBinding = DataBindingUtil.setContentView(this, R.layout.activity_rx_java);
        mBinding.btnSubscribe.setOnClickListener(this);
        mBinding.btnMap.setOnClickListener(this);
        mBinding
