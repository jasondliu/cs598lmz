import io.github.nandandesai.android_im_template.models.Message;
import io.github.nandandesai.android_im_template.service.ConnectionService;
import io.github.nandandesai.android_im_template.service.MessageService;
import io.github.nandandesai.android_im_template.ui.ChatActivity;
import io.github.nandandesai.android_im_template.ui.MessageListAdapter;

public class MessageListFragment extends Fragment {
    private MessageListAdapter messageListAdapter;
    private List<Message> messageList;
    private ConnectionService connectionService;
    private MessageService messageService;
    private Handler uiHandler;

    private RecyclerView messageRecyclerView;
    private Button sendMessageButton;
    private EditText messageInput;

    private String chatId;

    public MessageListFragment() {
        // Required empty public constructor
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
