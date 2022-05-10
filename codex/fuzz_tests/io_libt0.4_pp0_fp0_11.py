import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.CompositeDisposable;
import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;

public class LoginPresenter implements LoginContract.Presenter {

    private LoginContract.View mView;
    private DataManager dataManager;
    private CompositeDisposable compositeDisposable;

    public LoginPresenter(LoginContract.View mView, DataManager dataManager) {
        this.mView = mView;
        this.dataManager = dataManager;
        compositeDisposable = new CompositeDisposable();
    }

    @Override
    public void login(String username, String password) {
        mView.showLoading();
        Disposable disposable = dataManager.login(username,password)
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread
