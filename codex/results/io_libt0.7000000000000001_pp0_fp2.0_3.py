import io.realm.RealmResults;
import io.realm.Sort;

public class ViewEditExpense extends AppCompatActivity {
    private static final String TAG = "ViewEditExpense";

    //Variables
    private String expenseName, expenseAmount, expenseDate, expenseTime;
    private int expenseID;
    private TextView expenseNameTV, expenseAmountTV, expenseDateTV, expenseTimeTV;
    private FloatingActionButton editExpense;
    private Realm realm;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_edit_expense);

        //Initialize Realm
        realm = Realm.getDefaultInstance();

        //Get Intent Extras
        Intent intent = getIntent();
        expenseID = intent.getIntExtra("expenseID", 0);

        //Set up back button
        EditText editExpenseName = findViewById(R.id.editExpenseName);
        editExpenseName.setOnEditorActionListener(new TextView.OnEditorAction
