import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;
import okhttp3.ResponseBody;

/**
 * Created by Administrator on 2017/4/20 0020.
 */

public class LoginActivity extends BaseActivity<LoginActivityBinding> implements View.OnClickListener {

    private LoginViewModel mLoginViewModel;
    private RequestManager mRequestManager;
    private Context mContext;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        mContext = this;
        mRequestManager = Glide.with(this);
        setTitle("登录");
        showContentView();

        mLoginViewModel = new LoginViewModel(this);
        mLoginViewModel.setView(this);
        mLoginViewModel
