import io.reactivex.observers.TestObserver
import org.junit.Before
import org.junit.Test
import org.junit.runner.RunWith
import org.mockito.Mock
import org.mockito.Mockito
import org.mockito.MockitoAnnotations
import org.robolectric.RobolectricTestRunner


@RunWith(RobolectricTestRunner::class)
class RatesViewModelTest {

    @Mock
    private lateinit var localStorage: CurrencyRatesLocalStorage

    private lateinit var rateViewModel: RatesViewModel

    @Before
    fun setup() {
        MockitoAnnotations.initMocks(this)
        rateViewModel = RatesViewModel(localStorage)
    }

    @Test
    fun shouldDisplayInitialRates() {
        val rates = listOf("USDEUR")
        Mockito.`when`(localStorage.getAllCurrencies("USD")).thenReturn(Flowable.just(rates))
        val testListener = TestObserver<List<String>>()
        rate
