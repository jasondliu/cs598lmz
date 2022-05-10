import io.vertx.core.eventbus.EventBus;
import io.vertx.core.eventbus.MessageConsumer;
import io.vertx.core.eventbus.ReplyException;
import io.vertx.core.logging.Logger;
import io.vertx.core.logging.LoggerFactory;
import io.vertx.ext.bridge.PermittedOptions;
import io.vertx.ext.web.handler.sockjs.BridgeOptions;
import io.vertx.ext.web.handler.sockjs.SockJSHandler;
import org.vaadin.addon.calendar.item.BasicEventProvider;
import org.vaadin.addon.calendar.item.CalendarItem;
import org.vaadin.addon.calendar.item.EditableCalendarItemProvider;
import org.vaadin.addon.calendar.ui.CalendarComponentEvents;

import javax.servlet.http.HttpServletRequest;
import java.io.Serializable;
import java.util.Collection;
import java.util.Collections;
import java.
