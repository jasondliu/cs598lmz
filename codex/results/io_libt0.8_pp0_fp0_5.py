import io.reactivex.annotations.NonNull;
import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Consumer;
import io.reactivex.functions.Function;
import io.reactivex.functions.Predicate;

/**
 * Created by MirkoWu on 2017/3/16 0016.
 */

public class TestActivityGatherScene4 extends SuperBaseActivity {

    public static void openActivity(Context context) {
        Intent intent = new Intent(context, TestActivityGatherScene4.class);
        context.startActivity(intent);
    }

    @Override
    public int getContentViewID() {
        return R.layout.activity_test_gather_scene4;
    }

    @Override
    public void initData() {

    }

    @Override
    public void initUI() {
        scene1();
        scene2();
        scene3();
        scene4();
        scene5();
        scene6();
        scene7();
    }

    private void scene1() {

