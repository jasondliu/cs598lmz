import selectors from '../selectors';
import {
  getOrganizations,
  getStatuses,
  getSelectedOrganization,
  getSelectedStatus,
  getFilterQuery,
} from './organizations-selectors';

const defaultState = {
  organizations: [],
  statuses: [],
  selectedOrganization: null,
  selectedStatus: null,
  filterQuery: '',
};

describe('organizations selectors', () => {
  it('getOrganizations', () => {
    const actual = getOrganizations(defaultState);
    const expected = defaultState.organizations;
    expect(actual).toEqual(expected);
  });
  it('getStatuses', () => {
    const actual = getStatuses(defaultState);
    const expected = defaultState.statuses;
    expect(actual).toEqual(expected);
  });
  it('getSelectedOrganization', () => {
    const actual = getSelectedOrganization(defaultState);
    const expected = defaultState.selectedOrganization;
    expect(actual).to
