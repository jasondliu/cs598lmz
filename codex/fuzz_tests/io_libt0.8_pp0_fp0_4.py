import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;

public class SplashActivity extends BaseActivity {

    @BindView(R.id.splash_iv)
    ImageView splashIv;
    private SplashPresenter mSplashPresenter;
    private AVLoadingIndicatorView mAVLoadingIndicatorView;
    private TextView mTvSkip;

    @Override
    protected void initView() {
        setContentView(R.layout.activity_splash);
        ButterKnife.bind(this);
    }

    @Override
    protected void initData() {
        //初始化自定义控件
        initAVLoadingIndicatorView();
        //开始计时
        startAVLoadingIndicatorView(5);
        //初始化presenter
        initPresenter();
        //获取数据
        mSplashPresenter.getData();
    }

    /**
     * 初
