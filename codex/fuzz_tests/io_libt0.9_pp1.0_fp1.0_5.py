import io.cordova.zhihuiyingyuan.utils.SPUtils;
import io.cordova.zhihuiyingyuan.utils.ToastUtils;
import io.cordova.zhihuiyingyuan.utils.ViewUtils;
import io.cordova.zhihuiyingyuan.web.BaseWebActivity4;

/**
 * Created by Administrator on 2019/4/4 0004.
 */

public class AppNoticeListActivity extends BaseActivity implements View.OnClickListener {
    private static final int SCANNIN_GREQUEST_CODE = 1;

    private static final int SCANNIN_GREQUEST_CODE2 = 2;

    SharedPreferences sp;
    @BindView(R.id.tv_title)
    TextView tvTitle;

    @BindView(R.id.rl_title)
    RelativeLayout rlTitle;

    @BindView(R.id.rv_notice_list)
    RecyclerView rvNoticeList;

    @BindView(R.id.smart_refresh)
    SmartRefreshLayout
