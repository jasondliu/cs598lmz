import io.reactivex.schedulers.Schedulers;

/**
 * Created by yangfeng on 2017/6/23.
 */

public class LoginPresenter extends BasePresenter<LoginContract.View> implements LoginContract.Presenter {
    @Override
    public void login(String username, String password) {
        getView().showLoading();
        Api.getInstance().getApiService().login(username, password)
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Observer<User>() {
                    @Override
                    public void onSubscribe(Disposable d) {

                    }

                    @Override
                    public void onNext(User user) {
                        getView().hideLoading();
                        getView().onSuccess(user);
                    }

                    @Override
                    public void onError(Throwable e) {
                        getView().hideLoading();
                        getView().onError(e);
                    }

                    @Override
                    public void onComplete() {

                    }
