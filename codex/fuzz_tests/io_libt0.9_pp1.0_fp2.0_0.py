import io.vlingo.common.codec.StringCoder;

//TODO: transport
public class JournalEntryAdapter implements EventAdapter {
  private final Marshaller<Object> marshaller;
  private final Unmarshaller<Object> unmarshaller;

  public JournalEntryAdapter(final Marshaller<Object> marshaller, final Unmarshaller<Object> unmarshaller) {
    this.marshaller = marshaller;
    this.unmarshaller = unmarshaller;
  }

    @Override
    public void appendWith(DataOutput dataOutput, Object anEvent) throws IOException {
        final Object object = anEvent;
        final ObjectDataOutput dataOut = new ObjectDataOutput(dataOutput);
        final byte[] objectBytes = marshaller.marshall(object);
        dataOut.writeInt(objectBytes.length);
        dataOut.write(objectBytes);
    }

    @Override
    public <T> T fromJournalEntry(Class<T> expectedClass, DataInput dataInput) throws IOException {
        final ObjectData
