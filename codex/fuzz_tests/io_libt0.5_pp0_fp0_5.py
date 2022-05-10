import io.reactivex.disposables.Disposable
import io.reactivex.schedulers.Schedulers
import org.jetbrains.anko.toast
import java.util.concurrent.TimeUnit

/**
 * Created by Administrator on 2018/1/2.
 */
class LoginActivity : BaseActivity() {
    private lateinit var mEtMobile: EditText
    private lateinit var mEtCode: EditText
    private lateinit var mBtnCode: Button
    private lateinit var mBtnLogin: Button

    private var mTimeCount: TimeCount? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)

        initView()
    }

    private fun initView() {
        mEtMobile = findViewById(R.id.mEtMobile)
        mEtCode = findViewById(R.id.mEtCode)
        mBtnCode = findViewById(R.id.m
