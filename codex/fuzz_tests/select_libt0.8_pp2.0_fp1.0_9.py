import select_pic.selectPicUtil;

public class editActivity extends AppCompatActivity {
    private final String TAG = "editActivity";
    private String text,url;
    private int color,width,height,position;
    private selectPicUtil spu;
    private ImageView back,delete;
    private TextView save,text1,text2,text3,text4,text5;
    private EditText edit1,edit2,edit3,edit4,edit5;
    private EditText[] texts = {edit1,edit2,edit3,edit4,edit5};
    private TextView[] titles = {text1,text2,text3,text4,text5};
    private mySharedPreference msp;
    private Toolbar toolbar;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_edit);
        toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        getSupportActionBar().setDisplay
