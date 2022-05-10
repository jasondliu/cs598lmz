import io.reactivex.Observer;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;
import retrofit2.Retrofit;
import retrofit2.adapter.rxjava2.RxJava2CallAdapterFactory;
import retrofit2.converter.gson.GsonConverterFactory;

public class LoginActivity extends AppCompatActivity {

    private TextView home;
    private EditText phone;
    private EditText pwd;
    private Button login;
    private TextView reg;
    private ImageView qq;
    private ImageView weibo;
    private ImageView weixin;
    private static final int RESULT_LOGIN_CODE = 100;
    private static final int RESULT_REG_CODE = 101;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R
