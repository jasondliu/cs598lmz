import io.reactivex.Scheduler
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.schedulers.Schedulers
import kotlinx.android.synthetic.main.activity_login.*
import kotlinx.android.synthetic.main.activity_main.*
import java.util.*

class LoginActivity : AppCompatActivity(), LoginContract.View {

    private var loginPresenter: LoginPresenter? = null
    private var userModel: UserModel? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)
        loginPresenter = LoginPresenter(this)
        userModel = UserModel()

        buttonLogin.setOnClickListener {
            userModel?.login = editTextLogin.text.toString()
            userModel?.password = editTextPassword.text.toString()
            loginPresenter?.onClickLogin(userModel)
        }
    }
