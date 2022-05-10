import io.micrometer.core.instrument.MeterRegistry;
import io.micrometer.core.instrument.Tag;
import io.micrometer.core.instrument.Timer;
import io.micrometer.core.instrument.binder.MeterBinder;

/**
 * @author Heiko Scherrer
 */
@Conditional(MetricsCondition.class)
@Configuration
public class MetricsConfiguration {

    @Bean
    public MeterBinder customMetrics(MeterRegistry meterRegistry) {
        return new MeterBinder() {

            @Override
            public void bindTo(MeterRegistry registry) {
                Timer.builder("http.requests")
                    .tags(Arrays.asList(Tag.of("app", "dashboard")))
                    .register(registry);
            }
        };
    }
}
