import io.reactivex.disposables.Disposable;

/**
 * Created by 李杰 on 2019/9/25.
 */

public class EventDetailPresenter extends BasePresenter<EventDetailContract.View>
        implements EventDetailContract.Presenter{

    private DataManager manager;

    @Inject
    public EventDetailPresenter(DataManager manager) {
        this.manager = manager;
    }

    @Override
    public void sendEventDetailRequest(EventDetailRequest request) {
        addSubscribe(manager.sendEventDetailRequest(request)
                .compose(RxUtil.rxSchedulerHelper())
                .compose(RxUtil.handleResult2())
                .doOnSubscribe(new Consumer<Disposable>() {
                    @Override
                    public void accept(Disposable disposable) throws Exception {
                        mView.showLoading();
                    }
                })
                .subscribeWith(new BaseObserver<EventDetail>(mView) {
                    @Override
                    public void onNext(EventDetail eventDet
