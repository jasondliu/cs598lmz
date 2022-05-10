import selectSourceColorCode from '../selectors/sourceColorCode';
import { addSource, removeSource } from '../actions/sources';
import { changeSourceColor, removeSourceColor } from '../actions/sourceColors';
import { createColorCode, removeColorCode } from '../actions/colorCodes';
import { changeSourceDisplay, removeSourceDisplay } from '../actions/display';
import { changeSourceSortBy } from '../actions/sortBy';
import { changeSourceSorting, removeSourceSorting } from '../actions/sorting';
import { changeFeedLimit, removeFeedLimit } from '../actions/feedLimit';
import { changeSourceTextSearch } from '../actions/textSearch';
import { changeSourceFilterBy, removeSourceFilterBy } from '../actions/filterBy';
import { changeFeedType, toggleFeedType } from '../actions/feedType';
import { toggleFeedItemType, changeFeedItemType } from '../actions/feedItemType';
import { toggleFeedItemStatus, changeFeedItemStatus } from '../actions/feedItemStatus';
import { changeExportType } from '../actions
