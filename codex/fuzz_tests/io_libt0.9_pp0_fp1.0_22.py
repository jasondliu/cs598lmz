import io.vertx.ext.web.RoutingContext;
+import net.c0ffee.tailgatr.data.PushMessage;
+import net.c0ffee.tailgatr.data.Tailgate;
+import net.c0ffee.tailgatr.data.User;
+import net.c0ffee.tailgatr.persistance.TailgateProvider;
+import net.c0ffee.tailgatr.persistance.UserProvider;
+import net.c0ffee.tailgatr.push.PushService;
+
+public class TailgateController {
+
+	private UserProvider userProivder;
+	private TailgateProvider tailgateProivder;
+	private PushService pushService;
+	
+	public TailgateController(UserProvider userProvider, TailgateProvider tailgateProivder, PushService pushService) {
+		this.userProivder = userProvider;
+		this.tailgateProivder = tailgateProivder;
+		this.pushService = pushService;
+	}
+	
+	public
