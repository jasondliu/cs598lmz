import io.ipoli.android.app.utils.TimeFormatter;
import io.ipoli.android.app.utils.TimeOfDay;
import io.ipoli.android.quest.Quest;
import io.ipoli.android.quest.data.QuestStatus;
import io.ipoli.android.quest.viewmodels.QuestViewModel;

/**
 * Created by Venelin Valkov <venelin@curiousily.com>
 * on 4/30/16.
 */
public class BaseQuestViewModel {

    public final String id;
    public final String name;
    public final String startTime;
    public final String endTime;
    public final int lengthMinutes;
    public final int color;
    public final int statusColor;
    public final QuestStatus status;
    public final int priority;
    public final int finishNowButtonImage;
    public final boolean isRepeating;
    public final boolean isAllDay;

    public BaseQuestViewModel(Quest q) {
        id = q.getId();
        name = q.getName();
        startTime = TimeFormatter.
