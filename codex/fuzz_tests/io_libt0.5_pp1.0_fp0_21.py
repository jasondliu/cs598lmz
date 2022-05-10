import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;

public class SplashPresenter extends BasePresenter<SplashView> {
    private SplashView mView;
    private SplashModel mModel;

    public SplashPresenter(SplashView mView) {
        super(mView);
        this.mView = mView;
        mModel = new SplashModel();
    }

    public void getSplashData(int count) {
        mModel.getSplashData(count)
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Observer<SplashBean>() {
                    @Override
                    public void onSubscribe(Disposable d) {

                    }

                    @Override
                    public void onNext(SplashBean splashBean) {
                        mView.onSplashSuccess(splashBean);
                    }

                    @Override
                    public void onError(Throwable e) {
                       
