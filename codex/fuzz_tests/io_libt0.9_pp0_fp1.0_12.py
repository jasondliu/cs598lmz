import io.opensphere.analysis.table.model.TableColumnsModel;
import io.opensphere.analysis.table.model.ColumnType;
import io.opensphere.analysis.table.renderers.StringRenderer;
import io.opensphere.mantle.data.DataTypeInfo;
import io.opensphere.mantle.data.util.DataElementLookupUtils;

/**
 * Table for showing groupfied data in the table.
 */
public class GroupifyTable extends JTable
{
    /** The serialVersionUID. */
    private static final long serialVersionUID = 1L;

    /** The table model. */
    private final TableColumnsModel myTableModel;

    /**
     * Constructs a new table containing an image, a title and a message.
     *
     * @param tableModel the table model
     */
    public GroupifyTable(TableColumnsModel tableModel)
    {
        super(tableModel);

        myTableModel = tableModel;
        setRowHeight(myTableModel.getRowHeight());
        setAutoResizeMode(
