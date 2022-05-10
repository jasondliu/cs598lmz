import io.netty.channel.ChannelFuture;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.nio.NioServerSocketChannel;
import io.netty.channel.socket.SocketChannel;
import io.netty.handler.codec.DelimiterBasedFrameDecoder;
import io.netty.handler.codec.Delimiters;
import io.netty.handler.codec.string.StringDecoder;

import io.netty.bootstrap.*;

import io.netty.channel.ChannelOption;

import java.util.Scanner;

public class ChatServer{
	int port;
	public static ChannelGroup channelGroup;
	   
   public  ChatServer(int port){
		this.port = port;
	}
   
   public void run() throws Exception{
	   EventLoopGroup bossGroup = new NioEventLoopGroup();
	   EventLoopGroup workerGroup = new NioEventLoopGroup();
	   
	   try {
		   ServerBootstrap
