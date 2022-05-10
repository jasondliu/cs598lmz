import io.reactivex.schedulers.Schedulers;

/**
 * Created by Administrator on 2017/12/13.
 */

public class MyModel implements IModel {
    @Override
    public void getData(final OnFinishListener onFinishListener) {
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://www.zhaoapi.cn/")
                .addConverterFactory(GsonConverterFactory.create())
                .addCallAdapterFactory(RxJava2CallAdapterFactory.create())
                .build();
        ApiService apiService = retrofit.create(ApiService.class);
        Observable<Bean> observable = apiService.getData();
        observable.subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Observer<Bean>() {
                    @Override
                    public void onSubscribe(Disposable d) {

                    }

                    @Override
                    public void onNext(Bean bean) {
                        onFinishListener
