import selectedEntries from './selectedEntries';
import {
  SELECT_ENTRY,
  DESELECT_ENTRY,
  DESELECT_ALL_ENTRIES,
} from '../actions/types';

describe('selectedEntries reducer', () => {
  it('should return the initial state', () => {
    expect(selectedEntries(undefined, {})).toEqual([]);
  });

  it('should handle SELECT_ENTRY', () => {
    expect(
      selectedEntries([], {
        type: SELECT_ENTRY,
        entry: { id: '1', selected: true },
      })
    ).toEqual([{ id: '1', selected: true }]);

    expect(
      selectedEntries([{ id: '1', selected: true }], {
        type: SELECT_ENTRY,
        entry: { id: '2', selected: true },
      })
    ).toEqual([{ id: '1', selected: true }, { id: '2', selected: true }]);
  });

  it('should handle DESE
