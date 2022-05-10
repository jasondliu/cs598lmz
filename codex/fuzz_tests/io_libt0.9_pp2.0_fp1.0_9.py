import io.siddhi.query.api.definition.Attribute;
import org.apache.log4j.Logger;

import java.util.Locale;
import java.util.Map;

/**
 * Created by mahesh on 5/6/16.
 */
public class CountAggregator extends SiddhiAggregator {

    private static final Logger log = Logger.getLogger(CountAggregator.class);
    private CountStreamProcessor countStreamProcessor;

    public CountAggregator(CountStreamProcessor countStreamProcessor, ConfigReader configReader, StreamDefinition outputStreamDefinition) {
        this.countStreamProcessor = countStreamProcessor;
        this.configReader = configReader;
        this.outputStreamDefinition = outputStreamDefinition;
        this.outputStreamDefinition.attribute(countStreamProcessor.getReturnAttribute().getName(), Attribute.Type.DOUBLE);
    }

    public void process(ComplexEventChunk complexEventChunk) {
        complexEventChunk.reset();
        while (complexEventChunk.hasNext()) {
            ComplexEvent complex
