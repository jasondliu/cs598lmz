import io.vertx.ext.mail.MailClient;
import io.vertx.ext.mail.MailConfig;
import io.vertx.ext.mail.MailMessage;
import io.vertx.ext.mail.StartTLSOptions;

public class MailService {

    private MailClient client;

    public MailService(Vertx vertx, String host, int port, StartTLSOptions tls, String user, String password) {

        MailConfig mailConfig = new MailConfig();
        mailConfig.setHostname(host);
        mailConfig.setPort(port);
        mailConfig.setStarttls(tls);
        mailConfig.setUsername(user);
        mailConfig.setPassword(password);

        this.client = MailClient.createShared(vertx, mailConfig);
    }

    public void send(String subject, String message, String html, String from, String to, String cc, String bcc, Handler<AsyncResult<Void>> handler) {

        MailMessage mailMessage = new MailMessage();
        mailMessage.setFrom(from);
        mailMessage.setTo
