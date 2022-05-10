import io.confluent.examples.streams.utils.SpecificAvroDeserializer;
import io.confluent.examples.streams.utils.SpecificAvroSerializer;
import io.confluent.kafka.streams.serdes.avro.SpecificAvroSerde;
import org.apache.avro.specific.SpecificRecord;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.common.serialization.Serde;
import org.apache.kafka.streams.KafkaStreams;
import org.apache.kafka.streams.StreamsConfig;
import org.apache.kafka.streams.Topology;

import java.util.Properties;

/**
 * This example shows how you can use the SerializationExceptionHandler interface to handle exceptions
 * during deserialization and avoid crashes due to invalid messages.
 * <p>
 * This example driver assumes that the source topic has been pre-created and populated with the data
 * in {@link io.confluent.examples.streams.
