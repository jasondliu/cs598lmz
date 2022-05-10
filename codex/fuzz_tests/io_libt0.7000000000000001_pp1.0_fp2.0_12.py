import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "MainActivity";
    private Button btnRequest;
    private Button btnCancel;
    private Button btnRequest2;
    private Button btnRequest3;

    private TextView txtResponse;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        btnRequest = findViewById(R.id.btn_request);
        btnCancel = findViewById(R.id.btn_cancel);
        btnRequest2 = findViewById(R.id.btn_request2);
        btnRequest3 = findViewById(R.id.btn_request3);
        txtResponse = findViewById(R.id.txt_response);
        btnRequest.setOnClickListener(click -> request());

