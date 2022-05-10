import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;
import retrofit2.Response;

public class EditProfile extends AppCompatActivity {

    private String token;
    private String id;
    private String name;
    private String email;
    private String username;
    private TextInputEditText mName;
    private TextInputEditText mUsername;
    private TextInputEditText mEmail;
    private Button mSave;
    private Button mChangePassword;
    private ProgressBar mProgressBar;
    private ImageView mBack;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_edit_profile);

        initViews();

        token = getIntent().getStringExtra("token");
        id = getIntent().getStringExtra("id");
        name = getIntent().getStringExtra("name");
        email = getIntent().getStringExtra("email");
        username =
