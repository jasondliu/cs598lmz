import io.realm.Realm;
import io.realm.RealmResults;
import io.realm.Sort;

public class MemoActivity extends AppCompatActivity {

    private Realm realm;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_memo);
        ButterKnife.bind(this);

        Realm.init(this);
        //Get Realm instance
        realm = Realm.getDefaultInstance();


        setSupportActionBar((Toolbar) findViewById(R.id.toolbar));

        //Create the adapter that will return a fragment for each of the three
        //primary sections of the activity.

        List<Memo> memoList = new ArrayList<>();
        memoList.add(new Memo());


        MemoPagerAdapter memoPagerAdapter =
                new MemoPagerAdapter(getSupportFragmentManager(), memoList);

        //set up the ViewPager with the sections adapter.
        ViewPager viewPager = (ViewP
