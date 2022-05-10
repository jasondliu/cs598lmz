import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by Administrator on 2017/11/13.
 */

public class LoginPresenter extends BasePresenter<ILoginView> {

    private LoginModel loginModel;

    public LoginPresenter(ILoginView iLoginView) {
        super(iLoginView);
        loginModel = new LoginModel();
    }

    public void login(String username, String password) {
        loginModel.login(username, password)
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Observer<LoginBean>() {
                    @Override
                    public void onSubscribe(Disposable d) {

                    }

                    @Override
                    public void onNext(LoginBean loginBean) {
                        iView.loginSuccess(loginBean);
                    }

                    @Override
                    public void onError(Throwable e) {
                        iView.
