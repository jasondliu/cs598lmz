import io.reactivex.subjects.PublishSubject;

public class SplashActivity extends AppCompatActivity implements SplashView {

    @BindView(R.id.tv_splash)
    TextView tvSplash;

    private SplashPresenter splashPresenter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_splash);
        ButterKnife.bind(this);
        initPresenter();
        splashPresenter.getSplashImage(getString(R.string.splash_url));
    }

    private void initPresenter() {
        splashPresenter = new SplashPresenter(getLifecycle(), SplashActivity.this);
    }

    @Override
    public void onResponse(Splash splash) {
        ImageLoader.loadImage(tvSplash.getContext(), tvSplash, splash.getImg());
    }

    @Override
    public void onError(Throwable e) {

    }

    @Override
    public void onComplete() {


