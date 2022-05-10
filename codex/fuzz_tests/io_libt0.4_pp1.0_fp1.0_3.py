import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by Administrator on 2017/5/4 0004.
 */

public class HomePresenter implements HomeContract.Presenter {
    private HomeContract.View homeView;
    private HomeContract.Model homeModel;

    public HomePresenter(HomeContract.View homeView) {
        this.homeView = homeView;
        homeModel = new HomeModel();
    }

    @Override
    public void getHomeData(String url) {
        homeModel.getHomeData(url)
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Observer<HomeBean>() {
                    @Override
                    public void onSubscribe(Disposable d) {

                    }

                    @Override
                    public void onNext(HomeBean homeBean) {
                        homeView.getHomeDataSuccess(homeBean);
                    }

                    @Override
                   
