import selector from '../../selector';
import { onSetData, emptyArray, setData } from '../../helpers';

describe('Todos selector', () => {
  it('should create an empty list of todos when there is no data', () => {
    const fakeState = {
      todos: emptyArray,
    };

    const expected = {
      todos: [],
    };

    expect(selector(fakeState)).toEqual(expected);
  });

  it('should return the list of todos when there is data', () => {
    const fakeState = {
      todos: setData,
    };

    const expected = {
      todos: [
        {
          id: 1,
          title: 'learn react',
          completed: false,
        },
        {
          id: 2,
          title: 'learn redux',
          completed: false,
        },
        {
          id: 3,
          title: 'learn immutable',
          completed: false,
        },
      ],
    };

    expect(selector(
