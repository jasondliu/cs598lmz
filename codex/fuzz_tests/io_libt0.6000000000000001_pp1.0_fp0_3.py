import io.reactivex.Observable;
import io.reactivex.ObservableEmitter;
import io.reactivex.ObservableOnSubscribe;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by 7du-28 on 2018/1/29.
 */

public class UserModel {

    private static final String TAG = UserModel.class.getSimpleName();

    public interface OnLoginListener {
        void loginSuccess();

        void loginFailed();
    }

    public interface OnRegisterListener {
        void registerSuccess();

        void registerFailed();
    }

    public interface OnUpdateListener {
        void updateSuccess();

        void updateFailed();
    }

    public interface OnQueryListener {
        void querySuccess(List<User> list);

        void queryFailed();
    }

    public static void login(final String username, final String password, final OnLoginListener listener
