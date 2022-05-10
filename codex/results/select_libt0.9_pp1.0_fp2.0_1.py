import selectHotels from '../reducer';
import { initialState } from '../reducer';

describe('selectHotels Domain', () => {
  it('selects the initial state', () => {
    expect(selectHotels()).toMatchObject(initialState);
  });
});
