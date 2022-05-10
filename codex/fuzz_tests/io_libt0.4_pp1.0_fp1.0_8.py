import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;

public class MainPresenter extends MvpBasePresenter<MainView> {

    private final MainModel model;

    public MainPresenter() {
        model = new MainModel();
    }

    public void getData() {
        getViewState().showProgress();
        model.getData()
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Observer<List<Repo>>() {
                    @Override
                    public void onSubscribe(Disposable d) {

                    }

                    @Override
                    public void onNext(List<Repo> repos) {
                        getViewState().showData(repos);
                    }

                    @Override
                    public void onError(Throwable e) {
                        getViewState().showError(e.getMessage());
                    }

                    @Override
                    public void onComplete() {
                        getViewState().hideProgress
