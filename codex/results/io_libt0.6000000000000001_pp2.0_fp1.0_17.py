import io.github.softech.dev.sgill.domain.TimeCourseLog;
import io.github.softech.dev.sgill.domain.TimeCourseLogSearchRepository;
import io.github.softech.dev.sgill.repository.TimeCourseLogRepository;
import io.github.softech.dev.sgill.repository.search.TimeCourseLogSearchRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;


import java.util.Optional;

import static org.elasticsearch.index.query.QueryBuilders.*;

/**
 * Service Implementation for managing TimeCourseLog.
 */
@Service
@Transactional
public class TimeCourseLogService {

    private final Logger log = LoggerFactory.getLogger(TimeCourse
