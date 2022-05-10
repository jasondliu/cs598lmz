import io.reactivex.Single;
import io.reactivex.SingleObserver;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;
import retrofit2.Retrofit;

import static android.content.Context.MODE_PRIVATE;

public class UserLoginTask extends AsyncTask<Void, Void, Boolean> {

    private final String mEmail;
    private final String mPassword;
    private final Context mContext;
    private User mUser;
    private boolean mIsEmailExists;
    private boolean mIsPasswordCorrect;
    private boolean mIsCheckBoxChecked;
    private Auth auth;
    private SharedPreferences mPrefs;
    private SharedPreferences.Editor mPrefsEditor;
    private Retrofit retrofit;
    private IMyService iMyService;

    UserLoginTask(Context context, String email, String password, boolean isCheckBoxChecked) {
        mContext
