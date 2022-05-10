import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;

/**
 * @author: wuchao
 * @date: 2017/10/24 14:23
 * @desciption:
 */

public class GetTopMoviePresenter extends BasePresenter<GetTopMovieContract.View> implements GetTopMovieContract.Presenter {

    private DataManager mDataManager;
    private CompositeDisposable mCompositeDisposable;

    @Inject
    public GetTopMoviePresenter(DataManager dataManager) {
        this.mDataManager = dataManager;
        mCompositeDisposable = new CompositeDisposable();
    }

    @Override
    public void getTopMovie(int start, int count) {
        mCompositeDisposable.add(mDataManager.getTopMovie(start, count)
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Consumer<MovieSubject>()
