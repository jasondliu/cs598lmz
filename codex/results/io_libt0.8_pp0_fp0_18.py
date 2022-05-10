import io.reactivex.schedulers.Schedulers
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val api= RetrofitClient.instance.create(Api::class.java)
//        val store=getSharedPreferences("chan_it", Context.MODE_PRIVATE)
//        val user=store.getString("user","no user found")
//        user_name.text=user
        api.getHighLight().subscribeOn(Schedulers.io())
            .observeOn(AndroidSchedulers.mainThread())
            .subscribe(this::handleResponse)
    }

    private fun handleResponse(response: HighLight) {
        val adapter=HighLightAdapter(response.data)
        highLight.adapter=adapter
    }
}
