import io.reactivex.Observable
import io.reactivex.functions.BiFunction
import io.reactivex.schedulers.Schedulers
import io.reactivex.subjects.PublishSubject
import io.reactivex.subjects.Subject
import io.reactivex.subjects.UnicastSubject
import java.util.concurrent.TimeUnit

class ConversationsViewModel(private val session: Session) : BaseViewModel() {

    private val _conversations = MutableLiveData<List<Conversation>>()
    val conversations: LiveData<List<Conversation>> get() = _conversations
    private val _error = MutableLiveData<String>()
    val error: LiveData<String> get() = _error

    private val _newMessages = MutableLiveData<List<Message>>()
    val newMessages: LiveData<List<Message>> get() = _newMessages
    private val _newConversation = MutableLiveData<Unit>()
    val newConversation: LiveData<Unit> get()
