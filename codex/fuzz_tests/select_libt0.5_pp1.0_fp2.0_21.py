import selectedItems from '../../../../reducers/selectedItems';

const store = createStore(selectedItems);

describe('selectedItems reducer', () => {
  it('should handle initial state', () => {
    expect(
      selectedItems(undefined, {})
    ).toEqual([]);
  });

  it('should handle SELECT_ITEM', () => {
    expect(
      selectedItems([], {
        type: 'SELECT_ITEM',
        item: {
          id: 1,
          name: 'test',
          price: 1,
          quantity: 1,
          selected: true
        }
      })
    ).toEqual([{
      id: 1,
      name: 'test',
      price: 1,
      quantity: 1,
      selected: true
    }]);

    expect(
      selectedItems([{
        id: 1,
        name: 'test',
        price: 1,
        quantity: 1,
        selected: true
      }], {
        type: 'SELECT_ITEM',
        item: {

