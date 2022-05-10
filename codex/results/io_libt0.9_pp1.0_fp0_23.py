import io.reactivex.functions.Consumer
import org.greenrobot.eventbus.Subscribe
import org.greenrobot.eventbus.ThreadMode

class RecycleGoodsListActivity : BaseMvpRecycleListActivity<RecycleGoodsListBean, RecycleGoodsListBean.RecycleGoodsBean>() {

    private var id: Int = -1
    private var type: Int = -1//类型

    companion object {
        fun open(context: Context, type: Int, id: Int) {
            val bundle = Bundle()
            bundle.putInt("id", id)
            bundle.putInt("type", type)
            context.startActivity(Intent(context, RecycleGoodsListActivity::class.java).putExtras(bundle))
        }
    }

    override fun initRecyclerView() {
        mDataBinding?.recyclerview?.layoutManager = GridLayoutManager(this, 2)
        mDataBinding?.recyclerview?.adapter = adapter
    }

    override fun initPull
