import io.reactivex.schedulers.Schedulers;

/**
 * Created by Administrator on 2017/10/18.
 */

public class LoginModel implements LoginContract.Model {

    @Override
    public Observable<LoginBean> getLogin(String username, String password) {
        return RetrofitUtils.getInstance().getApiService().getLogin(username, password)
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread());
    }
}
