import io.reactivex.Observable;
import io.reactivex.ObservableEmitter;
import io.reactivex.ObservableOnSubscribe;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;
import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.RequestBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

/**
 * Created by Administrator on 2017/12/11.
 */

public class FileUploadActivity extends AppCompatActivity {
    private static final String TAG = "FileUploadActivity";
    private static final int REQUEST_CODE = 0x11;
    private static final int REQUEST_CODE_CHOOSE = 0x12;
    private static final int REQUEST_CODE_CAMERA = 0x13;
    private static final int REQUEST_CODE_CROP = 0
