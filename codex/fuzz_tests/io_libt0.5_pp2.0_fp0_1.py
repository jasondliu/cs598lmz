import io.reactivex.ObservableSource;
import io.reactivex.Observer;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Consumer;
import io.reactivex.functions.Function;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by wangjia on 2017/7/11.
 */

public class UserModel implements IUserModel {
    @Override
    public void login(final String username, final String password, final OnLoginListener loginListener) {
        Observable.just(username)
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .doOnNext(new Consumer<String>() {
                    @Override
                    public void accept(String s) throws Exception {
                        loginListener.onStart();
                    }
                })
                .observeOn(Schedulers
