import io.netty.handler.codec.http.multipart.InterfaceHttpData.HttpDataType;

public class MixedAttribute implements Attribute {
    private Attribute attribute;
    private int maxValueLength;
    private int size;

    public MixedAttribute(String name, int maxValueLength) {
        this.maxValueLength = maxValueLength;
        this.attribute = new MemoryAttribute(name);
    }

    public HttpDataType getHttpDataType() {
        return this.attribute.getHttpDataType();
    }

    public String getName() {
        return this.attribute.getName();
    }

    public int hashCode() {
        return this.attribute.hashCode();
    }

    public boolean equals(Object o) {
        return this.attribute.equals(o);
    }

    public int compareTo(InterfaceHttpData other) {
        return this.attribute.compareTo(other);
    }

    public String getValue() throws IOException {
        return this.attribute.getValue();
    }

    public void setValue(String value) throws
