import io.reactivex.schedulers.Schedulers

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        btn_load.setOnClickListener {
            loadData()
        }
    }

    private fun loadData() {
        val api = RetrofitClient.retrofit.create(ApiService::class.java)
        api.getUserData()
            .subscribeOn(Schedulers.io())
            .observeOn(AndroidSchedulers.mainThread())
            .subscribe({
                Log.d("MainActivity", it.get(0).name)
                Log.d("MainActivity", it.get(0).email)
                Log.d("MainActivity", it.get(0).address)
                Log.d("MainActivity", it.get(0).phone)
                Log.d("MainActivity", it.get(0).company)
            },{

