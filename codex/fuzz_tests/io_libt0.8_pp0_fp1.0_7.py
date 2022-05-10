import io.reactivex.schedulers.Schedulers

class MainProActivity : BaseActivity() {

    val mainModel: MainModel by lazy { MainModel(this) }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main_pro)
        RxView.clicks(findViewById(R.id.btn_test1))
                .throttleFirst(300, TimeUnit.MILLISECONDS)
                .subscribeOn(AndroidSchedulers.mainThread())
                .filter {
                    return@filter antiShakeClick()
                }
                .observeOn(Schedulers.io())
                .map {
                    return@map mainModel.test1()
                }
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(object : Observer<String> {
                    override fun onComplete() {

                    }

                    override fun onSubscribe(d: Disposable) {

                    }

                    override fun
