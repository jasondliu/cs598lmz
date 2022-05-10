import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "MainActivity";

    private static final String[] PERMISSIONS = {
            Manifest.permission.READ_EXTERNAL_STORAGE,
            Manifest.permission.WRITE_EXTERNAL_STORAGE
    };

    private static final int REQUEST_CODE_PERMISSIONS = 1;

    private static final int REQUEST_CODE_SELECT_VIDEO = 2;

    private static final int REQUEST_CODE_SELECT_IMAGE = 3;

    private static final int REQUEST_CODE_SELECT_AUDIO = 4;

    private static final int REQUEST_CODE_SELECT_FILE = 5;

    private static final int REQUEST_CODE_SELECT_DIR = 6;

    private static final int REQUEST_CODE_SELECT_VIDEO_AND_POSTER = 7;

    private static
