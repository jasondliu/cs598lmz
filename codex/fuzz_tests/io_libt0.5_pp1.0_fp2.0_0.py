import io.reactivex.Observable;
import io.reactivex.Observer;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;

import static com.example.lenovo.myapplication.utils.StaticClass.BASE_URL;

/**
 * Created by lenovo on 2018/8/18.
 * auther:lenovo
 * Date：2018/8/18
 */

public class UserModel extends BaseModel implements IUserModel {
    private static final String TAG = "UserModel";
    private Handler handler = new Handler();

    @Override
    public void login(final String account, String password, final IUserModel.OnLoginListener listener) {
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl(BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .addCallAdapterFactory(RxJava2CallAdapterFactory
