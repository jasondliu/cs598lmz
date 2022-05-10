import io.opentracing.propagation.TextMapExtractAdapter
import io.opentracing.propagation.TextMapInjectAdapter
import io.opentracing.tag.Tags
import io.opentracing.util.GlobalTracer
import io.reactivex.rxkotlin.subscribeBy
import io.reactivex.schedulers.Schedulers
import kotlinx.coroutines.experimental.async
import kotlinx.coroutines.experimental.runBlocking
import org.slf4j.LoggerFactory
import java.util.*

class Sender(
        private val mqttClient: MqttClient,
        private val baseTopic: String,
        private val maxReadingWidth: Int,
        private val maxReadingHeight: Int,
        private val maxReadingSize: Int
) {

    private val logger = LoggerFactory.getLogger(Sender::class.java)
    private val tracer: Tracer = GlobalTracer.get()

    fun sendReading(reading: RawReading, machineId:
