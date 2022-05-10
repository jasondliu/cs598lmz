import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.schedulers.Schedulers
import java.util.concurrent.TimeUnit
import javax.inject.Inject

class LoginViewModel @Inject constructor(
    private val apiService: ApiService,
    private val scheduler: SchedulerProvider,
    private val compositeDisposable: CompositeDisposable
) : ViewModel() {

    val loginFormState: MutableLiveData<LoginFormState> = MutableLiveData()
    val loginResult: MutableLiveData<LoginResult> = MutableLiveData()

    fun login(username: String, password: String) {
        // can be launched in a separate asynchronous job
        val disposable = apiService.login(LoginRequest(username, password))
            .subscribeOn(Schedulers.io())
            .observeOn(AndroidSchedulers.mainThread())
            .subscribe({
                val result = LoginResult
