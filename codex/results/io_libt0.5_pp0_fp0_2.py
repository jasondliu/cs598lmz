import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by huang on 2017/3/16.
 */

public class LoginPresenterImpl extends BasePresenterImpl<LoginContract.View> implements LoginContract.Presenter {

    private final DataManager mDataManager;

    @Inject
    public LoginPresenterImpl(DataManager dataManager) {
        mDataManager = dataManager;
    }

    @Override
    public void login(String username, String password) {
        Disposable disposable = mDataManager.login(username, password)
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(
                        new Consumer<Login>() {
                            @Override
                            public void accept(Login login) throws Exception {
                                mView.loginSuccess(login);
                            }
                        },

