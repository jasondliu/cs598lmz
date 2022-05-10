import io.reactivex.Observable;

/**
 * Created by ouko on 10/27/2017.
 */

public class WatchService extends Service {

    /**
     * Creates an IntentService.  Invoked by your subclass's constructor.
     *
     * @param name Used to name the worker thread, important only for debugging.
     */
    public WatchService() {
        super();
    }

    public static final String ACTION_SEND_MESSAGE = "SEND_MESSAGE";
    public static final String ACTION_GET_MESSAGE = "GET_MESSAGE";
    public static final String ACTION_GET_LAST_MESSAGE = "GET_LAST_MESSAGE";
    public static final String ACTION_SEND_MESSAGE_LIST = "SEND_MESSAGE_LIST";

    public static final String PARAM_MESSAGE = "message";
    public static final String PARAM_MESSAGE_LIST = "messages";
    public static final String PARAM_NOTIFICATION_ID = "not
