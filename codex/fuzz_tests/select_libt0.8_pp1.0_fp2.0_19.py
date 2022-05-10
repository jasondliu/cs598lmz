import selector from './selector';

describe('JoinRoomForm/selectors', () => {
  it('should handle state.joinRoomForm.isFetching', () => {
    const expected = true;
    const state = {
      joinRoomForm: {
        isFetching: true
      }
    };
    const next = selector({ joinRoomForm: state.joinRoomForm });

    expect(next.isFetching).toEqual(expected);
  });

  it('should handle state.joinRoomForm.error', () => {
    const expected = 'Oups something goes wrong';
    const state = {
      joinRoomForm: {
        error: expected
      }
    };
    const next = selector({ joinRoomForm: state.joinRoomForm });

    expect(next.error).toEqual(expected);
  });
});
