import io.reactivex.Observable
import io.reactivex.subjects.BehaviorSubject

class MainViewModel @Inject constructor(private val useCase: MainUseCase) : ViewModel() {
    private val mMessageSubject = BehaviorSubject.create<Message>()

    val message: Observable<Message>
        get() = mMessageSubject

    fun login(email: String, password: String) {
        useCase.execute(email, password)
            .subscribe({ data ->
                mMessageSubject.onNext(Message.SuccessLogin(data))
            }, { throwable ->
                mMessageSubject.onNext(Message.ErrorLogin(throwable))
            })
    }

    sealed class Message {
        data class SuccessLogin(val data: User) : Message()
        data class ErrorLogin(val throwable: Throwable) : Message()
    }
}
