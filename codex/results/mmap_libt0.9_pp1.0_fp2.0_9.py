import mmapi.MobileMessaging;
import mmapi.async.APIRequestHandler;

public class MobileCodesActivity extends Activity
{
  private TextView grcmTextView;
  private Button grcmAddButton;
  private EditText grcmEditText;
  private CheckBox grcmCheckBox;
  private ListView grcmListView;
  private ArrayAdapter<MobileCodesItem> adapter;

  @Override
  protected void onCreate(Bundle savedInstanceState)
  {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.mobile_codes);
    setTitle("Mobile Codes");

    grcmTextView = (TextView) findViewById(R.id.grcmTextView);
    grcmAddButton = (Button) findViewById(R.id.grcmAddButton);
    grcmEditText = (EditText) findViewById(R.id.grcmEditText);
    grcmCheckBox = (CheckBox) findViewById(R.id.grcmCheckBox);

    grcmListView = (ListView) findViewById(
