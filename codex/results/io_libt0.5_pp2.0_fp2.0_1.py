import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;

public class UserRxJavaActivity extends AppCompatActivity {

    @BindView(R.id.tv_result)
    TextView tvResult;
    @BindView(R.id.btn_login)
    Button btnLogin;
    @BindView(R.id.btn_register)
    Button btnRegister;
    @BindView(R.id.btn_get_user)
    Button btnGetUser;
    @BindView(R.id.btn_update_user)
    Button btnUpdateUser;
    @BindView(R.id.btn_upload_file)
    Button btnUploadFile;
    @BindView(R.id.btn_download_file)
    Button btnDownloadFile;
    @BindView(R.id.btn_download_file_with_progress)
    Button btnDownloadFileWithProgress;
    @BindView(R.id.btn_download_file_with_progress_and
