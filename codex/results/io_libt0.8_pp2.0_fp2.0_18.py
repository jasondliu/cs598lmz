import io.reactivex.functions.Action;
import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;


/**
 * Autho: hebin
 * <p>
 * Date: 16/8/1.
 * Description: 购物车
 */
public class CartFragment extends BaseFragment<CartPresenter> implements ICartView {

    @BindView(R.id.cart_list_rv)
    RecyclerView cartListRv;
    @BindView(R.id.cart_total_tv)
    TextView cartTotalTv;
    @BindView(R.id.cart_total_ll)
    LinearLayout cartTotalLl;
    @BindView(R.id.cart_settle_order)
    TextView cartSettleOrder;
    @BindView(R.id.cart_del_goods)
    TextView cartDelGoods;

    @BindView(R.id.cart_empty_view)
    ImageView cartEmptyView;

