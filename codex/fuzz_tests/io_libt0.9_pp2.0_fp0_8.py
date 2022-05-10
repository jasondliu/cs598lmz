import io.github.jhipster.web.util.ResponseUtil;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.net.URI;
import java.net.URISyntaxException;

import java.util.List;
import java.util.Optional;

/**
 * REST controller for managing MQuestStageCondition.
 */
@RestController
@RequestMapping("/api")
public class MQuestStageConditionResource {

    private final Logger log = LoggerFactory.getLogger(MQuestStageConditionResource.class);

    private static final String ENTITY_NAME = "mQuestStageCondition";

    private final MQuestStageConditionService mQuestStageConditionService;

    public MQuestStageConditionResource(MQuestStageConditionService mQuestStageConditionService) {
        this.mQuestStageConditionService = mQuestStageConditionService;
    }

    /**
     * POST  /m-quest-stage-cond
