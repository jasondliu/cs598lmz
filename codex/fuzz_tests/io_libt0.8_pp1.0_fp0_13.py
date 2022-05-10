import io.reactivex.functions.Consumer;
import io.reactivex.functions.Function;

/**
 * Created by Administrator on 2018/4/18 0018.
 */

public class HomeFragment extends BaseFragment {

    //导航栏
    private TabLayout mTabLayout;
    private ViewPager mViewPager;
    private List<Fragment> mFragment;
    private List<String> mTitle;
    private TabFragmentAdapter mAdapter;
    private Dialog dialog;
    private boolean isStop = false;

    @Override
    protected void initFragment(View view, Bundle savedInstanceState) {
        initView(view);
        setupViewPager();
    }

    private void initView(View view) {
        mTabLayout = (TabLayout) view.findViewById(R.id.tabLayout);
        mViewPager = (ViewPager) view.findViewById(R.id.viewPager);
        mTabLayout.setTabMode(TabLayout.MODE_FIXED);
        mTabLayout.setTab
