import io.reactivex.Observable;
import io.reactivex.ObservableEmitter;
import io.reactivex.ObservableOnSubscribe;
import io.reactivex.Observer;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;
import okhttp3.ResponseBody;

/**
 * Created by Administrator on 2017/10/17.
 */

public class UserModel implements IUserModel {

    private static final String TAG = "UserModel";

    @Override
    public void getUserData(final String userName, final String passWord, final CallBack callBack) {
        Observable.create(new ObservableOnSubscribe<ResponseBody>() {
            @Override
            public void subscribe(ObservableEmitter<ResponseBody> e) throws Exception {
                ResponseBody responseBody = NetWorkUtils.getInstance().getUserData(userName, passWord);
                e.onNext(
