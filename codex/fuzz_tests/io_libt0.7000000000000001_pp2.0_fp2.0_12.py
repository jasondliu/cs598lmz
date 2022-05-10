import io.netty.channel.ChannelHandlerContext;
import io.netty.handler.timeout.IdleStateEvent;
import io.netty.handler.timeout.IdleStateHandler;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.concurrent.TimeUnit;

/**
 * 空闲检测
 *
 * @author zuoyu
 * @program netty-practice
 * @create 2020-04-06 18:42
 **/
public class IMIdleStateHandler extends IdleStateHandler {

  private static final Logger logger = LoggerFactory.getLogger(IMIdleStateHandler.class);

  private static final int READER_IDLE_TIME = 15;

  public IMIdleStateHandler() {
    super(READER_IDLE_TIME, 0, 0, TimeUnit.SECONDS);
  }

  @Override
  protected void channelIdle(ChannelHandlerContext ctx, IdleStateEvent evt) throws Exception {
    logger.info("已
