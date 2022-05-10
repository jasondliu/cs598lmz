import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;

public class VerifyEmailActivity extends AppCompatActivity implements View.OnClickListener {

    private EditText etEmail;
    private TextView btVerify;
    private ProgressBar progressBar;
    private LinearLayout layoutRequest;

    VerifyEmailRequestDto dto = new VerifyEmailRequestDto();

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_verify_email);

        etEmail = findViewById(R.id.et_email);
        btVerify = findViewById(R.id.bt_verify);
        btVerify.setOnClickListener(this);
        progressBar = findViewById(R.id.progressBar);
        layoutRequest = findViewById(R.id.layout_request);
    }

    @Override
   
