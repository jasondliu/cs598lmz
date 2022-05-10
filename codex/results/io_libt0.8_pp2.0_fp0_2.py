import io.grpc.stub.ServerCalls.BidiStreamingMethod;
import io.grpc.stub.ServerCalls.ClientStreamingMethod;
import io.grpc.stub.ServerCalls.ServerStreamingMethod;
import io.grpc.stub.ServerCalls.UnaryMethod;
import io.grpc.stub.StreamObserver;

/**
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.27.0-SNAPSHOT)",
    comments = "Source: netty_server_skeleton.proto")
public final class NettyServerSkeletonGrpc {

  private NettyServerSkeletonGrpc() {}

  public static final String SERVICE_NAME = "NettyServerSkeleton";

  // Static method descriptors that strictly reflect the proto.
  private static volatile io.grpc.MethodDescriptor<netty_server_skeleton.NettyServerSkeleton.GString,
      netty_server_skeleton.NettyServerSkeleton.GString> getUpperMethod
