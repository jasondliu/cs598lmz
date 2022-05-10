import io.reactivex.schedulers.Schedulers;

/**
 * Created by Administrator on 2018/5/14.
 */

public class OrderDetailPresenter extends BasePresenter<OrderDetailView> {
    public OrderDetailPresenter(OrderDetailView baseView) {
        super(baseView);
    }

    public void getOrderDetail(String token, String order_id) {
        addDisposable(ApiRetrofit.getInstance().getApiService().getOrderDetail(token, order_id), new BaseObserver(baseView) {
            @Override
            public void onSuccess(Object o) {
                baseView.onOrderDetail((BaseModel<OrderDetailBean>) o);
            }

            @Override
            public void onError(String msg) {
                if (baseView != null) {
                    if ("连接错误".equals(msg)) {
                        baseView.onGetDataFail();
                    } else {
                        baseView.showError(msg);
                    }
                }

