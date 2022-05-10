import io.github.amorypepelu.library.mvp.BaseView;
import io.github.amorypepelu.third_ui.R;

/**
 * Created by pepelu on 2018/10/8.
 */
public class CoordinatorLayoutActivity extends BaseActivity {
    @Override
    protected String getFunctionName() {
        return "CoordinatorLayout + SnackBar";
    }

    @Override
    protected void beforeSetContent() {
        super.beforeSetContent();
    }

    @Override
    protected BasePresenter createPresenter() {
        return null;
    }

    @Override
    protected int provideContentViewId() {
        return R.layout.activity_coordinator_layout;
    }

    @Override
    protected void onResume() {
        super.onResume();
    }

    @Override
    public void onAttachedToWindow() {
        super.onAttachedToWindow();
    }

    @Override
    public void onDetachedFromWindow() {
        super.onDetachedFromWindow();
    }

    @
