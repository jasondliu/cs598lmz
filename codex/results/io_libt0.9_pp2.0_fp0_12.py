import io.durbs.stockstats.adapter.GoogleStockServiceAdapter;
import io.durbs.stockstats.domain.Stock;
import io.durbs.stockstats.domain.StockStats;
import io.durbs.stockstats.repository.StockStatsRepository;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import reactor.core.publisher.Mono;

import java.io.IOException;
import java.util.Collection;
import java.util.Optional;
import java.util.stream.Collectors;
import java.util.stream.Stream;

@Slf4j
@CrossOrigin(origins = {"http://localhost:3000", "http://localhost:5000", "http://localhost:8080"})
@RestController
@RequestMapping(value = "/stockstats")
public class StockStatsController {

    @Autowired
    private StockStatsRepository stockStats
