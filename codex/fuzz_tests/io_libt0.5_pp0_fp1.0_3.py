import io.reactivex.Observable
import io.reactivex.functions.BiFunction
import io.reactivex.subjects.PublishSubject
import java.util.concurrent.TimeUnit
import javax.inject.Inject

class QrScannerViewModel @Inject constructor(
    private val viewStateObservable: Observable<QrScannerViewState>,
    private val viewStateSubject: PublishSubject<QrScannerViewState>,
    private val interactor: QrScannerInteractor,
    private val router: QrScannerRouter
) : BaseViewModel() {

    init {
        viewStateObservable
            .debounce(200, TimeUnit.MILLISECONDS)
            .observeOn(Schedulers.io())
            .map { it.qrCode }
            .distinctUntilChanged()
            .switchMap {
                Observable.zip(
                    interactor.getWalletIdByAddress(it),
                    interactor.getWalletIdByPrivateKey(it),
                    BiFunction { addressId:
