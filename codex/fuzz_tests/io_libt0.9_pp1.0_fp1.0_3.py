import io.github.hedgehog1029.overwatch.cmd.pool.PoolRegistry;
import io.github.hedgehog1029.overwatch.cmd.perms.PermissionsManager;
import io.github.hedgehog1029.overwatch.perms.Rank;

public class CommandHandler implements ICommandHandler {
	private static volatile List<RegisteredCommand> pool;
	private static volatile List<Messageable> messageables;

	public static void setPool(List<RegisteredCommand> pool) {
		CommandHandler.pool = pool;
	}

	public static void setMessageables(List<Messageable> listeners) {
		CommandHandler.messageables = listeners;
	}

	/**
	 * Partitions the passed String into a String[] with the delimiter of " " (space).
	 *
	 * @para
