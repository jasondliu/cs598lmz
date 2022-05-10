import io.reactivex.disposables.Disposable
import io.reactivex.schedulers.Schedulers
import io.reactivex.subjects.PublishSubject
import uk.co.droidinactu.exerciseplanner.App
import uk.co.droidinactu.exerciseplanner.RoomDb.Eq


class EqDao(val eqDao: EqDao) {
    private val eqs = PublishSubject.create<List<Eq>>()

    init {
        eqDao.getAll().subscribeOn(Schedulers.io()).observeOn(AndroidSchedulers.mainThread()).subscribe { eqs -> this.eqs.onNext(eqs) }
    }

    fun getAll(): Flowable<List<Eq>> {
        return eqs.toFlowable(BackpressureStrategy.LATEST)
    }

    fun addEq(eq: Eq): Completable {
        return Completable.fromAction { eqDao.addEq(
