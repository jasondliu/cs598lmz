import io.rsbox.api.GameState
import io.rsbox.api.Server
import io.rsbox.api.ServerProperties
import io.rsbox.api.World
import io.rsbox.api.entity.GroundItem
import io.rsbox.api.entity.Npc
import io.rsbox.api.entity.Player
import io.rsbox.api.item.Item
import io.rsbox.api.plugin.Plugin
import io.rsbox.api.plugin.PluginManifest
import io.rsbox.api.plugin.PluginState
import io.rsbox.engine.ServerScheduler
import io.rsbox.engine.net.game.MessagePipeline
import io.rsbox.engine.sync.task.TickSyncTask
import io.rsbox.net.game.GameConnection
import io.rsbox.util.Timer
import org.tinylog.Logger
import java.util.concurrent.atomic.AtomicBoolean
import kotlin.reflect.KClass

/**
 * A game service that represents a single game.
 *
 * @author Kyle
