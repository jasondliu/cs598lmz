import io.reactivex.schedulers.Schedulers;
import retrofit2.Response;

/**
 * Created by KomoriWu
 * on 2017-05-24.
 */

public class PicturePresenter extends BasePresenter<PictureContract.View> implements PictureContract.Presenter {
    @Override
    public void getPicture() {
        RetrofitHelper.getInstance().getApiService()
                .getBeautiful(ApiService.BASE_URL)
                .compose(getView().<Response<BeautifulGson>>bindToLife())
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Observer<Response<BeautifulGson>>() {
                    @Override
                    public void onSubscribe(Disposable d) {

                    }

                    @Override
                    public void onNext(Response<BeautifulGson> response) {
                        getView().setPicture(response.body().getResults());
                    }

                    @Override
                    public void onError(Throwable e)
