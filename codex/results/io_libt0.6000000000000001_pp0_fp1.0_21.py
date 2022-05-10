import io.reactivex.Observable
import io.reactivex.disposables.Disposable
import io.reactivex.schedulers.Schedulers
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.list_row.*
import kotlinx.android.synthetic.main.list_row.view.*
import java.util.concurrent.TimeUnit

class MainActivity : AppCompatActivity() {

    private var adapter: ListAdapter? = null

    private var disposable: Disposable? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        initRecyclerView()
        createObservable()
    }

    private fun initRecyclerView() {
        adapter = ListAdapter(this)
        listRecyclerView.layoutManager = LinearLayoutManager(this)
        listRecyclerView.adapter = adapter
    }
