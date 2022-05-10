import io.reactivex.Observable;

/**
 * Created by Administrator on 2018/6/25.
 */

public class PayModel implements PayContract.Model {
    @Override
    public Observable<BaseResponse> pay(String productId, String userId, String type) {
        return RetrofitUtil.getInstance().getmApiService().pay(userId, productId, type);
    }
}
