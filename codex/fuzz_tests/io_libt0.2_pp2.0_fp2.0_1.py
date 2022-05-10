import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by Administrator on 2018/1/11.
 */

public class LoginPresenter extends BasePresenter<LoginContract.View> implements LoginContract.Presenter {
    private LoginContract.Model model;

    public LoginPresenter() {
        model = new LoginModel();
    }

    @Override
    public void login(String username, String password) {
        if (TextUtils.isEmpty(username)) {
            mView.showError("用户名不能为空");
            return;
        }
        if (TextUtils.isEmpty(password)) {
            mView.showError("密码不能为空");
            return;
        }
        mView.showLoading();
        addSubscribe(model.login(username, password)
                .subscribeOn(Schedulers.io())
                .
