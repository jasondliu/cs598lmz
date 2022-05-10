import io.reactivex.disposables.Disposable;

public class RemindVM extends BaseViewModel {
    public MutableLiveData<RemindBean> remind = new MutableLiveData<>();

    public RemindVM(@NonNull Application application) {
        super(application);
    }

    public void getData(String uid,String token) {
        UserService userService = retrofit.create(UserService.class);
        Disposable subscribe = userService.getRemind(uid, token)
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Consumer<RemindBean>() {
                    @Override
                    public void accept(RemindBean remindBean) throws Exception {
                        remind.setValue(remindBean);
                    }
                }, new Consumer<Throwable>() {
                    @Override
                    public void accept(Throwable throwable) throws Exception {
                        if (throwable instanceof HttpException) {
                            HttpException httpException =
