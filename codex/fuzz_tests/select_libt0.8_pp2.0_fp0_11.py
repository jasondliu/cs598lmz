import selectTimeout from './selectTimeout';
import { setTimeout } from '../../actions';

describe('selectTimeout', () => {
  it('should select the timeout', () => {
    const timeout = 30000;
    const mockedState = fromJS({
      settings: {
        timeout,
      },
    });
    expect(selectTimeout(mockedState)).toEqual(timeout);
  });
});

describe('selectTimeout', () => {
  it('should select the timeout', () => {
    const timeout = 30000;
    const mockedState = fromJS({
      settings: {
        timeout,
      },
    });
    expect(selectTimeout(mockedState)).toEqual(timeout);
  });
});

describe('mapDispatchToProps', () => {
  const dispatchMock = jest.fn();
  const props = mapDispatchToProps(dispatchMock);

  it('should call dispatch when called setTimeout', () => {
    props.setTimeout(0);
    expect(dispatchMock).toHaveBeenCalledWith
