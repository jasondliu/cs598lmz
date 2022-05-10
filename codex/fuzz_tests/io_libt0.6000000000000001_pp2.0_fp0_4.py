import io.netty.util.concurrent.EventExecutorGroup;
import io.netty.util.concurrent.Future;
import io.netty.util.concurrent.GenericFutureListener;

import java.net.SocketAddress;
import java.util.List;
import java.util.Map;

import org.apache.log4j.Logger;

import com.google.common.collect.Lists;
import com.google.common.collect.Maps;

import net.sf.json.JSONObject;
import top.lshaci.framework.common.model.BaseEntity;
import top.lshaci.framework.utils.StringUtils;

/**
 * <p>Title: ChannelHandlerContextUtils</p>
 * <p>Description: ChannelHandlerContext utils</p>
 * <p>Company: com.lshaci</p>
 * @author lshaci
 * @date 2017年9月1日下午4:59:57
 * @version 1.0
 * @since 1.0
 */
public final class ChannelHandlerContext
