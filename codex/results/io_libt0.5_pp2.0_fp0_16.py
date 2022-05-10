import io.reactivex.schedulers.Schedulers
import kotlinx.android.synthetic.main.activity_main.*
import java.util.concurrent.TimeUnit

class MainActivity : AppCompatActivity() {

    private lateinit var disposable: Disposable

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        disposable = Observable.fromIterable(1..100)
            .subscribeOn(Schedulers.computation())
            .map {
                Thread.sleep(100)
                "Mapped $it"
            }
            .observeOn(AndroidSchedulers.mainThread())
            .subscribe {
                Log.i("MainActivity", "Received $it")
                textView.text = it
            }

    }

    override fun onDestroy() {
        super.onDestroy()
        disposable.dispose()
    }
}
