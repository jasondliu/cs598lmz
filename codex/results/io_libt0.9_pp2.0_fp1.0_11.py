import io.rong.imkit.RongIM;
import io.rong.imkit.RongIM.ConversationBehaviorListener;
import io.rong.imkit.manager.IUnReadMessageObserver;
import io.rong.imkit.model.UIConversation;
import io.rong.imlib.RongIMClient.ConnectCallback;
import io.rong.imlib.model.Conversation;
import io.rong.imlib.model.Message;
import io.rong.imlib.model.Message.ReceivedStatus;
import io.rong.imlib.model.UserInfo;

public class Homeactivity extends FragmentActivity implements OnClickListener, IUnReadMessageObserver, ConversationBehaviorListener {
	private String TAG="Homeactivity";
	private ImageView[] mTabs;
	private Fragment[] fragments;
	private int index;
	private int currentTabIndex;
	private TextView unreadLabel;
	public static final int LISTEN_LOGIN_SUCCESS = 0;
	static {
		/*
