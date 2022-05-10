import io.reactivex.Observable;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by Administrator on 2017/5/12.
 */

public class SignInActivity extends BaseActivity implements View.OnClickListener {
    private ImageView mImageView;
    private EditText mEditText;
    private Button mButton;
    private TextView mTextView;
    private String mUserName;
    private String mPassword;
    private Disposable mDisposable;

    @Override
    protected int getLayoutId() {
        return R.layout.activity_signin;
    }

    @Override
    protected void initData() {

    }

    @Override
    protected void initView() {
        mImageView = (ImageView) findViewById(R.id.iv_signin_back);
        mEdit
