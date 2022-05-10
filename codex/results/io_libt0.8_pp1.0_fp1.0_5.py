import io.netty.buffer.ByteBuf;
//import io.netty.buffer.Unpooled;
//import lombok.Data;
//
///**
// * Created by luorijie on 2017/5/29.
// */
//@Data
//public class RpcResponse {
//    private String requestId;
//    private String error;
//    private Object result;
//    private ByteBuf buffer;
//
//    public boolean isError() {
//        return error != null;
//    }
//
//    public ByteBuf encode(SerializeSupport serializer) {
//        if (buffer == null) {
//            buffer = serializer.writeObject(this);
//        }
//        return buffer;
//    }
//
//    public static RpcResponse from(ByteBuf buf, SerializeSupport serializer) {
//        RpcResponse response = serializer.readObject(buf, RpcResponse.class);
//        response.buffer = Unpooled.wrappedBuffer(buf);
//        return response;
//    }
//}
