import io.reactivex.functions.BiFunction;
import io.reactivex.functions.Consumer;
import io.reactivex.functions.Function;
import io.reactivex.schedulers.Schedulers;

public class RxJavaOperatorActivity extends AppCompatActivity {
    private static final String TAG = RxJavaOperatorActivity.class.getSimpleName();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_rx_java_operator);
        initView();
    }

    private void initView() {
        findViewById(R.id.btn_map).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                map();
            }
        });

        findViewById(R.id.btn_flatMap).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                flatMap();
           
