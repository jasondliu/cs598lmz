import io.netty.buffer.ByteBuf;
import io.netty.buffer.Unpooled;

import java.util.Iterator;
import java.util.LinkedList;

import edu.wpi.first.wpilibj.networktables.NetworkTable;
import edu.wpi.first.wpilibj.tables.IRemote;
import edu.wpi.first.wpilibj.tables.IRemoteConnectionListener;
import edu.wpi.first.wpilibj.tables.ITable;
import edu.wpi.first.wpilibj.tables.ITableListener;

public class Connection {
	private final ConnectionAdapter adapter;
	private final Object lock;
	private final LinkedList queue;
	private boolean isDead;
	private boolean isAlive;
	private static final int MAX_QUEUE_SIZE_BEFORE_WARNING = 10000;
	private final IRemote remote;
	private final int id;

	public Connection(ConnectionAdapter adapter) {
		this(adapter, (IRemote)null);
