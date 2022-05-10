import io.spine.server.storage.jdbc.DataSourceWrapper;
import io.spine.server.storage.jdbc.DataSourceWrapperFactory;
import io.spine.server.storage.jdbc.table.RecordTable;
import io.spine.server.storage.jdbc.type.JdbcColumn;

import java.sql.SQLException;
import java.util.Iterator;
import java.util.Optional;

import static com.google.common.base.Preconditions.checkNotNull;
import static com.google.common.base.Preconditions.checkState;
import static io.spine.server.storage.jdbc.message.MessageTable.messageTable;
import static io.spine.server.storage.jdbc.message.MessageTableColumn.ID;
import static io.spine.server.storage.jdbc.message.MessageTableColumn.MESSAGE_BYTES;
import static io.spine.server.storage.jdbc.message.MessageTableColumn.MESSAGE_TYPE;
