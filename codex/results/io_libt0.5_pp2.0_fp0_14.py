import io.github.luizgrp.sectionedrecyclerviewadapter.SectionedRecyclerViewAdapter;
import io.github.luizgrp.sectionedrecyclerviewadapter.StatelessSection;

public class SectionedRecyclerViewActivity extends AppCompatActivity {

    private static final String TAG = SectionedRecyclerViewActivity.class.getSimpleName();

    private SectionedRecyclerViewAdapter sectionAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sectioned_recycler_view);

        sectionAdapter = new SectionedRecyclerViewAdapter();

        sectionAdapter.addSection(new NewsSection(getString(R.string.header_news), getNews()));
        sectionAdapter.addSection(new NewsSection(getString(R.string.header_events), getEvents()));

        RecyclerView recyclerView = (RecyclerView) findViewById(R.id.recyclerview);
        recyclerView.set
