import io.reactivex.schedulers.Schedulers;

/**
 * 作者： xj Tu
 * 时间： 2019/3/20
 * 描述：
 */
public class Model {

    public static void getData(final CallBack callBack){
        ApiService apiserver = HttpUtils.getInstance().getApiserver(ApiService.url, ApiService.class);
        Observable<Bean> getdata = apiserver.getData();
        getdata.subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Observer<Bean>() {
                    @Override
                    public void onSubscribe(Disposable d) {

                    }

                    @Override
                    public void onNext(Bean bean) {
                        callBack.onSuccess(bean);
                    }

                    @Override
                    public void onError(Throwable e) {
                        callBack.onFail(e.toString());
                    }
