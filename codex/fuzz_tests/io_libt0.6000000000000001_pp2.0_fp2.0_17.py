import io.github.nixtabyte.telegram.jtelebot.server.impl.AbstractCommandDispatcher;
import io.github.nixtabyte.telegram.jtelebot.server.impl.DefaultCommandDispatcher;
import io.github.nixtabyte.telegram.jtelebot.server.impl.DefaultCommandQueue;
import io.github.nixtabyte.telegram.jtelebot.server.impl.DefaultCommandWatcher;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadFactory;

import org.apache.commons.configuration.Configuration;
import org.apache.commons.lang.Validate;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * This is the main class of the TelegramBot API.
 *
 * @author Knut Jorda
 * @author Ruben Bermudez
 * @version 0.3
 * @see <a href="https://core.telegram.org/bots
