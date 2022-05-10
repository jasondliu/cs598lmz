import io.reactivex.Single;
import io.reactivex.functions.Function;
import io.reactivex.schedulers.Schedulers;

public class LoginActivity extends BaseActivity<ActivityLoginBinding, LoginViewModel> implements LoginNavigator {

    private static final String TAG = LoginActivity.class.getSimpleName();
    private LoginViewModel loginViewModel;
    private ActivityLoginBinding activityLoginBinding;

    @Override
    public int getBindingVariable() {
        return BR.viewModel;
    }

    @Override
    public int getLayoutId() {
        return R.layout.activity_login;
    }

    @Override
    public LoginViewModel getViewModel() {
        loginViewModel = ViewModelProviders.of(this).get(LoginViewModel.class);
        return loginViewModel;
    }

    @Override
    public void handleError(Throwable throwable) {
        Log.d(TAG, "handleError: " + throwable);
    }

    @Override
    public void login() {
        String email = activity
