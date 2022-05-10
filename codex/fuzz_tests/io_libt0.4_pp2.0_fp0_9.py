import io.reactivex.Observable;
import io.reactivex.ObservableOnSubscribe;
import io.reactivex.Observer;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;

import static com.example.myapplication.utils.NetworkUtils.getConnectivityStatusString;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "MainActivity";

    private RecyclerView rvNews;
    private NewsAdapter mNewsAdapter;
    private ProgressBar progressBar;
    private SwipeRefreshLayout swipeRefreshLayout;
    private TextView tvError;
    private Button btnRetry;
    private CoordinatorLayout coordinatorLayout;

    private List<Article> articles = new ArrayList<>();
    private String TAG_FOR_TOAST = "toast";
    private String TAG_FOR_SNACKBAR = "snackbar";
    private String TAG_
