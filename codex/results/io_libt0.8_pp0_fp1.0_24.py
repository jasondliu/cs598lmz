import io.reactivex.Single
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.schedulers.Schedulers
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import java.text.SimpleDateFormat
import java.util.*

class DetailActivity : AppCompatActivity() {

  private lateinit var viewModel: DetailActivityViewModel

  private lateinit var client: ApiClient

  private lateinit var compositeDisposable: CompositeDisposable

  private lateinit var jobAdapter: JobAdapter


  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.activity_detail)
    setSupportActionBar(toolbar)

    compositeDisposable = CompositeDisposable()

    client = ApiClient.create()

    viewModel = ViewModelProviders.of(this).get(DetailActivityViewModel::class
