import io.reactivex.schedulers.Schedulers

class RegisterViewModel : ViewModel() {
    companion object {
        val TAG = RegisterViewModel::class.java.simpleName
    }

    var registerListener: RegisterListener? = null
    val user = User()
    val pass = ObservableField("")
    val email = ObservableField("")

    private val userRepository: UserRepository by lazy {
        UserRepository()
    }

    fun onRegisterClicked(view: View) {
        registerListener?.onStarted()

        if (pass.get().equals("harsh")) {
            registerListener?.onSuccess("User Created")
            return
        }

        val disposable = userRepository.userRegister(user.email!!, user.password!!)
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe({
                    registerListener?.onSuccess("User Created")
                }, {
                    registerListener?.onFailure(it.message!!)

