import io.reactivex.schedulers.Schedulers;

/**
 * @author ThinkPad
 * @date 2018/8/9 15:50
 */
public class MyPresenter {
    private String TAG = "MyPresenter";

    private MyView view;
    private MyModelImpl model;

    public MyPresenter(MyView view) {
        this.view = view;
        model = new MyModelImpl();
    }

    public void login(String phone, String pwd) {
        model.login(phone, pwd)
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Observer<LoginBean>() {
                    @Override
                    public void onSubscribe(Disposable d) {
                        Log.e(TAG, "onSubscribe: " + d);
                    }

                    @Override
                    public void onNext(LoginBean loginBean) {
                        Log.e(TAG, "onNext: " + loginBean.toString());
                        view.login
