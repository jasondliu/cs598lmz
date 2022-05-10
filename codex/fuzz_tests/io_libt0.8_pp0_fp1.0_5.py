import io.reactivex.disposables.Disposable;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.WebSocket;
import okhttp3.WebSocketListener;
import okio.ByteString;

public class WebSocketFragment extends Fragment {

    private Disposable disposable;
    private Disposable interval;
    private WebSocket mWebSocket;
    private boolean isClosed = false;

    private OkHttpClient mClient;
    private Request mRequest;
    private RequestBody requestBody = RequestBody.create("Hello, World".getBytes());
    private RequestBody pingRequestBody = RequestBody.create(ByteString.decodeHex("FA5B5F5A"));

    public WebSocketFragment() {
        // Required empty public constructor
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container
