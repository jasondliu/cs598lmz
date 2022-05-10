import io.netty.buffer.Unpooled;
import io.netty.util.CharsetUtil;
import lombok.extern.slf4j.Slf4j;

import java.util.Random;

/**
 * @author leon on 6/7/16.
 */
@Slf4j
@ChannelHandler.Sharable
public class SendHandler extends ChannelInboundHandlerAdapter {

  private final Random random = new Random();
  private ByteBuf message;
  private int MSG_SIZE = 1000;

  public SendHandler(int MSG_SIZE) {
    this.MSG_SIZE = MSG_SIZE;
  }

  @Override
  public void channelActive(ChannelHandlerContext ctx) throws Exception {
    message = ctx.alloc().buffer(MSG_SIZE);
    for (int i = 0; i < message.capacity(); i ++) {
      message.writeByte((byte) i);
    }
  }

  @Override
  public void channelRead(ChannelHandlerContext ctx, Object msg) thr
