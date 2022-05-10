import io.reactivex.schedulers.Schedulers;

/**
 * Created by Administrator on 2016/3/16.
 */
public class SellReturnGoodsListPresenter extends BasePresenter<ISellReturnGoodsListView> {
    public SellReturnGoodsListActivity mContext;
    public SellReturnGoodsListModel model;

    public SellReturnGoodsListPresenter(SellReturnGoodsListActivity mContext) {
        this.mContext = mContext;
        model = new SellReturnGoodsListModel();
    }

    //获取销售退货单列表
    public void getSellReturnOrderList(int PageIndex, int PageSize, String Status, String StarTime, String EndTime, String SearchKey, String DeptId) {
        String data = model.getSellReturnOrderList(PageIndex, PageSize, Status, StarTime, EndTime, SearchKey, DeptId);
        getCompositeSubscription().add(manager.getSellReturnOrderList(data)
                .subscribeOn(Sched
