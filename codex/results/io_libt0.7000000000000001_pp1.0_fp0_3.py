import io.reactivex.observers.TestObserver
import io.reactivex.schedulers.TestScheduler
import io.reactivex.subjects.PublishSubject
import java.util.concurrent.TimeUnit

class MainPresenterTest {

    val view = mock<MainContract.View>()
    val repository = mock<MainContract.Repository>()
    val scheduler = TestScheduler()
    val presenter = MainPresenter(view, repository, scheduler)
    val observer = TestObserver<List<Item>>()

    @Before
    fun `Set up`() {
        whenever(repository.fetchData()).thenReturn(Observable.just(listOf(Item("", ""))))
        whenever(view.searchText()).thenReturn(PublishSubject.create())
    }

    @Test
    fun `When user enters search text, it should trigger search`() {
        presenter.start()
        verify(view, times(1)).searchText()
    }

    @Test
    fun `When user enters search text, it should fetch
