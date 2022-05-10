import io.reactivex.schedulers.Schedulers;

/**
 * Created by Administrator on 2018/1/15.
 */

public class LoginPresenter extends BasePresenter<LoginView> {
    private LoginModel loginModel;

    public LoginPresenter(LoginView baseView) {
        super(baseView);
    }

    @Override
    protected void initModel() {
        loginModel = new LoginModel();
        addModel(loginModel);
    }

    public void login(String userName, String password) {
        baseView.showLoading();
        loginModel.login(userName, password)
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new BaseObserver<LoginBean>(baseView) {
                    @Override
                    public void onSuccess(LoginBean o) {
                        if (o != null) {
                            baseView.onSuccess(o);
                        }
                    }

                    @Override
                    public void onError(String msg) {
                       
