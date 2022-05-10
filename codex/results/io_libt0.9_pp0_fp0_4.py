import io.reactivex.Observable
import io.reactivex.functions.Consumer
import io.reactivex.schedulers.Schedulers
import org.greenrobot.eventbus.EventBus
import org.greenrobot.eventbus.Subscribe
import org.greenrobot.eventbus.ThreadMode
import wulkanowy.api.WUClass
import wulkanowy.api.forums.ForumReplies
import wulkanowy.api.forums.ForumTopic
import wulkanowy.events.NotificationChangeEvent
import wulkanowy.services.NotificationChangeReceiver.Companion.ACTION_CLOSE_NOTIFICATION
import wulkanowy.services.NotificationChangeReceiver.Companion.ACTION_OPEN_NOTIFICATION
import wulkanowy.utils.observeOnMainThread

class NotificationChangeReceiver : WakefulBroadcastReceiver() {

    companion object {
        const val ACTION_CLOSE_NOTIFICATION = "wulkanowy.services.ACTION_CLOSE_NOTIFICATION"
        const val ACTION_OPEN_NOTIFIC
