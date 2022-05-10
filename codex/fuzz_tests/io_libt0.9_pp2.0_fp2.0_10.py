import io.vertigo.audit.domain.Audit;
import io.vertigo.audit.impl.dao.AuditDAO;
import io.vertigo.audit.impl.dao.EventTypeDataBase;
import io.vertigo.audit.impl.dao.EventTypeStore;
import io.vertigo.audit.impl.dao.formater.FieldFormater;
import io.vertigo.audit.impl.dao.formater.FieldFormaterChain;
import io.vertigo.core.App;
import io.vertigo.core.Home;
import io.vertigo.core.config.AppConfig;
import io.vertigo.core.config.AppConfigBuilder;
import io.vertigo.database.sql.SqlManager;
import io.vertigo.database.sql.connection.SqlConnection;
import io.vertigo.database.sql.vendor.SqlDataBase;
import io.vertigo.database.sql.vendor.SqlDataBaseManager;

/**
 * Initialisation des tables de l'audit.
 *
