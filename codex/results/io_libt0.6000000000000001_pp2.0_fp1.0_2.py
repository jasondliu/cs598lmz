import io.reactivex.annotations.NonNull;
import io.reactivex.disposables.CompositeDisposable;
import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Consumer;

public abstract class BaseActivity<T extends BasePresenter> extends RxAppCompatActivity implements BaseView {

    protected T mPresenter;
    private CompositeDisposable mCompositeDisposable;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(getLayoutId());
        initPresenter();
        if (mPresenter != null) {
            mPresenter.attachView();
        }
        initView();
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (mPresenter != null) {
            mPresenter.detachView();
        }
        unSubscribe();
    }

    protected abstract int getLayoutId();

    protected abstract void initView();

    protected
