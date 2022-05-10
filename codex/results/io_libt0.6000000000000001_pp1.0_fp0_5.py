import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;
import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.RequestBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

import static com.example.cse110.flashbackmusic.PlaybackService.PAUSE;
import static com.example.cse110.flashbackmusic.PlaybackService.PLAY;
import static com.example.cse110.flashbackmusic.PlaybackService.RESUME;
import static com.example.cse110.flashbackmusic.PlaybackService.SKIP;

public class MainActivity extends AppCompatActivity implements View.OnClickListener, OnMapReadyCallback,
        GoogleApiClient.ConnectionCallbacks, GoogleApiClient.OnConnectionFailedListener,
        LocationListener, OnDialogFragmentInteractionListener {

    private static final String TAG = "MainActivity";
    private static final int REQUEST_CODE = 0;
    private
