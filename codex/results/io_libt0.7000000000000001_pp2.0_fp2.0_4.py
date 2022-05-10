import io.reactivex.schedulers.Schedulers;

public class LoginPresenter extends BasePresenter<LoginContract.IView> implements LoginContract.IPresenter {

    private LoginContract.IModel mModel;

    public LoginPresenter() {
        mModel = new LoginModel();
    }

    @Override
    public void login(String userName, String password) {
        mModel.login(userName, password)
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Observer<LoginEntity>() {
                    @Override
                    public void onSubscribe(Disposable d) {
                        mCompositeDisposable.add(d);
                    }

                    @Override
                    public void onNext(LoginEntity loginEntity) {
                        mView.loginSuccess(loginEntity);
                    }

                    @Override
                    public void onError(Throwable e) {
                        mView.loginError(e);
                    }

                    @Override
                    public void onComplete() {

