import io.socket.client.Socket;
import io.socket.emitter.Emitter;
import io.socket.engineio.client.transports.WebSocket;

public class ChatActivity extends AppCompatActivity {

    private EditText mInputMessageView;
    private ListView mMessagesView;
    private Button mSend;
    private String name;
    private String room;

    private RecyclerView mMessagesRecyclerView;
    private MessageAdapter mAdapter;
    private List<Message> mMessages = new ArrayList<Message>();

    private Socket mSocket;
    {
        try {
            mSocket = IO.socket(Constants.CHAT_SERVER_URL);
            mSocket.io().transports(new WebSocket.NAME);

        } catch (URISyntaxException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_chat);

        Intent intent = getInt
