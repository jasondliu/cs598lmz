import io.reactivex.schedulers.Schedulers
import org.junit.Before
import org.junit.Test
import org.mockito.Mock
import org.mockito.Mockito
import org.mockito.MockitoAnnotations


class MainPresenterTest{


    private lateinit var presenter: MainPresenter

    @Mock
    private lateinit var view: MainView

    @Mock
    private lateinit var userDataSource: UserDataSource

    @Before
    fun setup() {
        MockitoAnnotations.initMocks(this)
        presenter = MainPresenter(view, userDataSource)
    }

    @Test
    fun `should call show error if device internet connection is off`() {
        Mockito.`when`(userDataSource.isNetworkAvailable()).thenReturn(false)

        presenter.getUsers()

        Mockito.verify(view).showNetworkError()

    }
    @Test
    fun `should call show loading on call`() {
        Mockito.`when`(userDataSource.
