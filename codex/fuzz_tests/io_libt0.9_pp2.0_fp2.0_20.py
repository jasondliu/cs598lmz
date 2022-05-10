import io.github.cactacea.backend.core.infrastructure.validators.ValueValidator
import io.github.cactacea.backend.core.util.responses.CactaceaErrors.{UserAlreadyBlocked, InvalidReportUserId}
import io.github.cactacea.backend.core.domain.models.User
import io.github.cactacea.backend.core.infrastructure.dao._
import io.github.cactacea.backend.core.infrastructure.identifiers.{SessionId, UserId}
import io.github.cactacea.backend.core.util.exceptions.CactaceaException
import io.github.cactacea.backend.core.util.responses.CactaceaErrors

class ReportsDAO @Inject()(
                            val sessi
