import io.nadron.client.util.ObjectBeanUtil;
import io.nadron.client.util.ObjectCloner;

import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;
import java.util.concurrent.ConcurrentHashMap;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


/**
 * This class will act as a cache for the user session. It will create a new
 * user session when ever the user logs into the system. It will also make sure
 * the session is cleaned up on logout.
 * 
 * @author Abraham Menacherry
 * 
 */
public class UserSessionCache
{
	private static final Logger LOG = LoggerFactory
			.getLogger(UserSessionCache.class);
	/**
	 * Key will be the user name, value will be the session object.
	 */
	private Map<String, UserSession> userSessionMap;
	
