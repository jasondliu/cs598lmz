import io.stockgeeks.spring.kafka.stockstatsaggregator.model.CoffeeDrinkerCount;
import io.stockgeeks.spring.kafka.stockstatsaggregator.model.StockStats;
import lombok.extern.slf4j.Slf4j;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.support.KafkaHeaders;
import org.springframework.messaging.handler.annotation.Header;
import org.springframework.messaging.handler.annotation.Payload;
import org.springframework.stereotype.Component;

@Slf4j
@Component
public class StockStatsConsumer {

  private final StockStatsRepository stockStatsRepository;

  public StockStatsConsumer(StockStatsRepository stockStatsRepository) {
    this.stockStatsRepository = stockStatsRepository;
  }

  @KafkaListener(topics = Topics.STOCK_STATS)
  public void consume(@Payload StockStats stats, @Header(
