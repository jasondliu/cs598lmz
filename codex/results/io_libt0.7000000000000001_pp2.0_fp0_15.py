import io.reactivex.schedulers.Schedulers;

/**
 * Created by Administrator on 2018/7/19.
 */

public class MainPresenter extends BasePresenter<MainModel, MainContract.View> implements MainContract.Presenter {
    @Override
    public void getData(HashMap<String, String> params) {
        if (!isViewAttached()) {
            return;
        }
        mView.showLoading();
        mModel.getData(params)
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Observer<MainBean>() {
                    @Override
                    public void onSubscribe(Disposable d) {

                    }

                    @Override
                    public void onNext(MainBean mainBean) {
                        mView.onSuccess(mainBean);
                    }

                    @Override
                    public void onError(Throwable e) {
                        mView.onError(e.getMessage());
       
