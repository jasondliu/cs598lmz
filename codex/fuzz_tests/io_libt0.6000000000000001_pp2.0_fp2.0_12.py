import io.reactivex.schedulers.Schedulers
import kotlinx.android.synthetic.main.activity_main.*
import org.koin.android.ext.android.inject
import org.koin.android.viewmodel.ext.android.viewModel

class MainActivity : AppCompatActivity(), ActionBar.TabListener, DrawerLayout.DrawerListener {

    private val viewModel: MainViewModel by viewModel()
    private val drawerToggle: ActionBarDrawerToggle by inject()
    private val adapter: ViewPagerAdapter by inject()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        viewPager.adapter = adapter
        tabs.setupWithViewPager(viewPager)
        drawer.addDrawerListener(this)
        drawerToggle.syncState()
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        supportActionBar?.setHomeButtonEnabled(true)
        supportActionBar?
