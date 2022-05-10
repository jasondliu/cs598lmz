import io.grpc.ServerServiceDefinition;
import com.google.protobuf.AbstractMessage;

@javax.annotation.Generated("by GAPIC")
public class GreeterGrpc {
  private GreeterGrpc() {}

  public static final String SERVICE_NAME = "helloworld.Greeter";

  // Static method descriptors that strictly reflect the proto.
  @io.grpc.ExperimentalApi
  public static final io.grpc.MethodDescriptor<com.example.grpc.helloworld.HelloRequest,
      com.example.grpc.helloworld.HelloReply> METHOD_SAY_HELLO =
      io.grpc.MethodDescriptor.<com.example.grpc.helloworld.HelloRequest, com.example.grpc.helloworld.HelloReply>newBuilder()
          .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
          .setFullMethodName(generateFullMethodName(
              "helloworld.Greeter", "SayHello"))
          .setRequestMarshaller(
