import selectors from '../../../selectors/selectors';
import { getDataFromState } from '../../../utils/getDataFromState';
import { getIdsFromState } from '../../../utils/getIdsFromState';

export const getData = createSelector(
  [getDataFromState('teamMembers'), getIdsFromState('teamMembers')],
  (data, ids) => {
    return data.map(item => ({
      ...item,
      id: ids[item.id],
    }));
  },
);

export const getTeamMembers = createSelector(
  [getData, selectors.teamMembers.getTeamMembers],
  (data, teamMembers) =>
    data.filter(item => teamMembers[item.id] && teamMembers[item.id].isActive),
);

export const getTeamMembersIds = createSelector(
  [getTeamMembers],
  teamMembers => teamMembers.map(item => item.id),
);

export const getTeamMembersData = createSelector(
  [getTeamMembersId
