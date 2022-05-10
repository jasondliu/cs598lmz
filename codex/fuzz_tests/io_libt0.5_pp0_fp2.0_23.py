import io.reactivex.disposables.Disposable
import io.reactivex.functions.Function
import io.reactivex.schedulers.Schedulers
import kotlinx.android.synthetic.main.activity_main.*
import java.util.concurrent.TimeUnit

class MainActivity : AppCompatActivity() {

    private val viewModel: MainViewModel by lazy { ViewModelProviders.of(this).get(MainViewModel::class.java) }

    private val disposable: Disposable by lazy {
        RxView.clicks(button)
                .throttleFirst(1, TimeUnit.SECONDS)
                .observeOn(Schedulers.io())
                .flatMap { viewModel.getMessage() }
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe({
                    textView.text = it
                }, {
                    textView.text = "Error"
                })
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(s
