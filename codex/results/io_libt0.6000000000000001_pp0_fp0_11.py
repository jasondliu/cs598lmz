import io.reactivex.Observable;
import io.reactivex.Observer;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Consumer;
import io.reactivex.functions.Function;
import io.reactivex.schedulers.Schedulers;
import okhttp3.ResponseBody;
import retrofit2.Response;

/**
 * Created by Administrator on 2017/9/27.
 */

public class LoginPresenter extends BasePresenter<LoginContract.View> implements LoginContract.Presenter {
    private LoginContract.View loginView;
    private LoginContract.Model loginModel;
    public LoginPresenter(LoginContract.View loginView) {
        this.loginView=loginView;
        loginModel=new LoginModel();
    }
    @Override
    public void login(String username, String password) {
        loginView.showProgress();
        loginModel.login(username,password)
                .
