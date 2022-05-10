import io.netty.channel.DefaultChannelId;
import io.netty.util.NetUtil;
import io.netty.util.internal.SystemPropertyUtil;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Locale;
import java.util.regex.Pattern;

import static io.netty.resolver.HostsFileParser.parseIp4;
import static io.netty.resolver.HostsFileParser.parseIp6;

/**
 * A {@link HostsFileEntriesResolver} that loads the <a href="http://www.iana.org/domains/root/db">root name servers</a>
 * from a {@code hosts} file that is bundled with the distributed JAR file of this library.
 *
 * @see HostsFileEntriesResolverBuilder#parseSilently()
 */
public final class RootNameServerAddressResolverGroup extends HostsFileEntriesResolverGroup {

    private static final Pattern WH
