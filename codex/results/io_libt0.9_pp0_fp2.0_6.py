import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by scott on 2018/9/19.
 */
public class SearchActivity extends AppCompatActivity {

    private Toolbar toolbar;
    private EditText mEtSearch;
    private Button mBtnSearch;
    private RecyclerView mRvList;


    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_search);

        initView();
    }

    private void initView() {
        toolbar = (Toolbar) findViewById(R.id.toolbar);
        toolbar.setNavigationOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
            }
        });

        mEtSearch = (EditText) findViewById(R.id.et_search);
        mBtnSearch = (Button
