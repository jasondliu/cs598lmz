import selectedGroupReducer from './selectedGroup.reducer';
import selectedGroupMemberReducer from './selectedGroupMember.reducer';
import markedProfileReducer from './markedProfile.reducer';
import selectedTeamMemberReducer from './selectedTeamMember.reducer';
import profileReducer from './profile.reducer';
import localStorageReducer from './localStorage.reducer';
import userReducer from './user.reducer';
import commentReducer from './comment.reducer'
import teamInfoReducer from './teamInfo.reducer';
import markedPostReducer from './markedPost.reducer';

const rootReducer = combineReducers({
    feed: feedReducer,
    selectedFeed: selectedFeedReducer,
    selectedGroup: selectedGroupReducer,
    selectedGroupMember: selectedGroupMemberReducer,
    markedProfile: markedProfileReducer,
    selectedTeamMember: selectedTeamMemberReducer,
    profile: profileReducer,
    localStorage: localStorageReducer,
    user: userReducer,
    comment: commentReducer,
   
