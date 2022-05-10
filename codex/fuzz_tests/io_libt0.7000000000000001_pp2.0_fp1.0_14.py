import io.reactivex.schedulers.Schedulers;

public class MyBalancePresenter extends BasePresenter<MyBalanceContract.View> implements MyBalanceContract.Presenter {
    private final MyBalanceService mService;

    public MyBalancePresenter(MyBalanceContract.View view) {
        super(view);
        mService = RetrofitFactory.createService(MyBalanceService.class);
    }

    @Override
    public void getBalance() {
        mService.getBalance(LoginHelper.getInstance().getUserToken())
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Subscriber<BaseResponse<Balance>>() {
                    @Override
                    public void onCompleted() {

                    }

                    @Override
                    public void onError(Throwable e) {
                        LogUtils.d(e.toString());
                    }

                    @Override
                    public void onNext(BaseResponse<Balance> balanceBaseResponse) {
                        if (balanceBaseResponse.isSuccess()) {

