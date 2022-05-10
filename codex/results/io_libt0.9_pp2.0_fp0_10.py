import io.realm.Realm;
import io.realm.RealmConfiguration;
import io.realm.RealmQuery;

public class AddArtistActivity extends AppCompatActivity {

    private ImageButton mFoto;
    private TextInputEditText mNombre;
    private TextInputEditText mApellido;
    private TextInputEditText mBiografia;
    private TextInputEditText mId;
    private int mTestId;
    private Uri imageUri;
    private ScrollView mScrollView;
    private Artist mArtist;
    private RealmQuery<Artist> mQuery;
    private TextInputLayout mNombreContainer;
    private TextInputLayout mApellidoContainer;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_artist);
        mNombre = (TextInputEditText) findViewById(R.id.name_edit_text);
        mScrollView = (ScrollView) findViewById(R.id.
