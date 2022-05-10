import io.realm.RealmList;
import io.realm.RealmResults;

public class BListActivity extends BaseActivity implements SwipeRefreshLayout.OnRefreshListener {
    private static final int REQUEST_IMAGE_CAPTURE = 1;
    private static final int REQUEST_STORAGE_PERMISSION = 1;

    private static final String TAG = BListActivity.class.getSimpleName();
    @BindView(R.id.toolbar)
    Toolbar mToolbar;
    @BindView(R.id.layout_empty)
    RelativeLayout mLayoutEmpty;
    @BindView(R.id.recyler)
    RecyclerView mRecycler;
    @BindView(R.id.swipe_refresh)
    SwipeRefreshLayout mSwipeRefresh;

    private FilesAdapter mAdapter;


    private static String[] PERMISSIONS_STORAGE = {
            Manifest.permission.READ_EXTERNAL_STORAGE,
            Manifest.permission.WRITE_EXTERNAL_STORAGE
    };


