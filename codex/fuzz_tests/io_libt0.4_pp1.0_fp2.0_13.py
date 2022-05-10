import io.reactivex.Observer;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by Administrator on 2018/8/10.
 */

public class TestPresenter extends BasePresenter<TestContract.View> implements TestContract.Presenter {

    @Override
    public void getData() {
        RetrofitFactory.getInstance().getApiService().getData()
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Observer<TestBean>() {
                    @Override
                    public void onSubscribe(Disposable d) {

                    }

                    @Override
                    public void onNext(TestBean testBean) {
                        if (mView != null) {
                            mView.getDataSuccess(testBean);
                        }
                    }

                    @Override
                    public
