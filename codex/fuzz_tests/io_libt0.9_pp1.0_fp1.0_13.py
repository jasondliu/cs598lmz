import io.netty.buffer.ByteBuf
import io.netty.channel.{ChannelHandlerContext, ChannelInboundHandlerAdapter}

class SocketInboundHandler extends ChannelInboundHandlerAdapter {

  override def channelRead(ctx: ChannelHandlerContext, msg: Any): Unit = {
    var bytebuf: ByteBuf = null
    try {
      bytebuf = msg.asInstanceOf[ByteBuf]
      val receive:Array[Byte] = new Array[Byte](bytebuf.readableBytes())
      bytebuf.readBytes(receive)
      val body = new String(receive,"utf-8")
      println(s"接收到：${body}")
      ctx.writeAndFlush(ByteBufUtils.download(body, bytebuf))
    } catch {
      case e:Exception => e.printStackTrace()
    } finally {
      if (bytebuf != null) {
        ReferenceCountUtil.release(bytebuf)
      }
    }

  }
}
