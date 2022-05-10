import io.github.prepayments.data.filing.message.notifications.FileUploadNotification;
import io.github.prepayments.data.filing.streams.notifications.FileUploadStreams;
import lombok.extern.slf4j.Slf4j;
import org.springframework.jms.annotation.JmsListener;
import org.springframework.messaging.handler.annotation.Headers;
import org.springframework.messaging.handler.annotation.Payload;
import org.springframework.stereotype.Component;

import java.time.LocalDateTime;
import java.util.Map;

@Slf4j
@Component("fileUploadNotificationListener")
public class FileUploadNotificationListener {

    private final FileUploadNotificationService fileUploadNotificationService;

    public FileUploadNotificationListener(final FileUploadNotificationService fileUploadNotificationService) {
        this.fileUploadNotificationService = fileUploadNotificationService;
    }

    /**
     * Listener to ingest the excel file uploaded notification message and persist it
    
