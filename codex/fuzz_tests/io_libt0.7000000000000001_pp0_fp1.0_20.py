import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by Administrator on 2018/3/1 0001.
 */

public class MoviePresenter implements MovieContract.IMoviePresenter {
    private MovieContract.IMovieModel mModel;
    private MovieContract.IMovieView mView;
    private CompositeDisposable mCompositeDisposable = new CompositeDisposable();

    public MoviePresenter(MovieContract.IMovieView iMovieView) {
        mModel = new MovieModel();
        mView = iMovieView;
    }

    @Override
    public void loadData() {
        Disposable disposable = mModel.execute().subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Consumer<Movie>() {
                    @Override
                    public void accept(Movie movie) throws Exception {
                        mView.showData(movie);

