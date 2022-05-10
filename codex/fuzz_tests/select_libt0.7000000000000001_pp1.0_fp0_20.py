import select from '../select';
import { fromJS } from 'immutable';
import expect from 'expect';

const selector = select.makeSelectFormDomain();

describe('makeSelectFormDomain', () => {
  it('should select the form state', () => {
    const formState = fromJS({
      form: {},
    });
    const mockedState = fromJS({
      form: formState,
    });

    expect(selector(mockedState)).toEqual(formState);
  });
});
