import io.reactivex.schedulers.Schedulers
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {


    private lateinit var adapter: ForecastAdapter
    private lateinit var viewModel: ForecastViewModel
    private lateinit var forecastData: MutableList<Forecast>

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        forecastData = mutableListOf()
        adapter = ForecastAdapter(forecastData, this)

        viewModel = ViewModelProviders.of(this).get(ForecastViewModel::class.java)

        viewModel.getForecastData().observe(this, Observer {
            forecastData.clear()
            forecastData.addAll(it)
            adapter.notifyDataSetChanged()
        })

        viewModel.getForecastData()
        viewModel.getForecastDataWithZip()

        rv_forecast.layoutManager
