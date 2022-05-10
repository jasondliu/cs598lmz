import io.circe.generic.auto._
import io.circe.syntax._
import javax.inject._
import org.joda.time.DateTime
import play.api.mvc._
import play.api.libs.circe.Circe
import services.{ConfigurationService, EmailService, FileService, FormService, UserService}
import utils.{Contexts, Implicits, Mailer}

import scala.concurrent.{ExecutionContext, Future}

/**
 * @author Louis Vialar
 */
class FormController @Inject()(cc: ControllerComponents, formService: FormService, userService: UserService, files: FileService, emailService: EmailService, config: ConfigurationService)(implicit ec: ExecutionContext) extends AbstractController(cc) with Circe with Implicits with Contexts {
  import FormController._

  private def getForm(id: Int)(implicit req: RequestHeader): Option[Form] = formService.getForm(id)

  def getForms: Action[Unit] = Action.async(circe.
