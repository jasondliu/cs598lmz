import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;
import okhttp3.ResponseBody;

public class SettingActivity extends BaseActivity {

    @BindView(R.id.tb_setting)
    Toolbar toolbar;
    @BindView(R.id.sw_vibrate)
    Switch swVibrate;
    @BindView(R.id.tv_bluetooth)
    TextView tvBluetooth;
    @BindView(R.id.tv_firmware_version)
    TextView tvFirmwareVersion;
    @BindView(R.id.btn_logout)
    Button btnLogout;
    private ProgressDialog progressDialog;
    private Disposable disposable;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_setting);
        ButterKn
