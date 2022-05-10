import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "MainActivity";
    private static final int REQUEST_CODE = 100;

    private String[] permissions = {Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_COARSE_LOCATION, Manifest.permission.WRITE_EXTERNAL_STORAGE};
    private List<String> mPermissionList = new ArrayList<>();

    private AppCompatButton mBtn_normal;
    private AppCompatButton mBtn_rx;
    private AppCompatButton mBtn_retrofit;
    private AppCompatButton mBtn_retrofit_rx;
    private AppCompatButton mBtn_download;
    private AppCompatButton mBtn_download_rx;
    private AppCompatButton mBtn_upload;
