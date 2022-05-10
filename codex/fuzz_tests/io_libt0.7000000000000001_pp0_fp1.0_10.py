import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.CompositeDisposable;
import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class ProfileActivity extends AppCompatActivity {
    private static final String TAG = "ProfileActivity";
    private TextView name, email, phone, dateOfBirth, gender, bloodGroup;
    private ImageView profileImage;
    private Button btnEditProfile;
    private String mUserId, mUserName, mUserEmail;
    private String mPhone, mDateOfBirth, mGender, mBloodGroup, mProfileImage;
    private String mTempImagePath;
    private ProgressDialog mProgressDialog;
    private IUserService iUserService;
    private IUploadAPI iUploadAPI;

