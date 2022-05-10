import io.github.lucaseasedup.logit.exceptions.IllegalProfileException;
import io.github.lucaseasedup.logit.util.PlayerUtils;
import io.github.lucaseasedup.logit.util.org.apache.commons.lang3.StringUtils;
import java.util.List;
import java.util.Map;
import java.util.logging.Level;
import org.bukkit.Bukkit;
import org.bukkit.Location;
import org.bukkit.entity.Player;

public final class TeleportAction implements AccountAction
{
    @Override
    public String getName()
    {
        return "tp";
    }
    
    @Override
    public String getDescription()
    {
        return "Teleports a player to the specified location."
                + " If a location is not specified, player will be teleported"
                + " to the location saved in the LogIt's data storage.";
    }
    
    @Override
    public String getUsage()
    {
        return "[
