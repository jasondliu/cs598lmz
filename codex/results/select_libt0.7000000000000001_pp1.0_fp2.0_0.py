import selectors from '../../selectors/expenses';
import expenses from '../fixtures/expenses';
import moment from 'moment';

test('should filter by text value', () => {
    const filters = {
        text: 'e',
        sortBy: 'date',
        startDate: undefined,
        endDate: undefined
    };
    const result = selectors(expenses, filters);
    expect(result).toEqual([ expenses[2], expenses[1] ]);
});

test('should filter by startDate', () => {
    const filters = {
        text: '',
        sortBy: 'date',
        startDate: moment(0),
        endDate: undefined
    };
    const result = selectors(expenses, filters);
    expect(result).toEqual([ expenses[2], expenses[0] ]);
});

test('should filter by endDate', () => {
    const filters = {
        text: '',
        sortBy: 'date',
        startDate: undefined,
        endDate: moment(0).add(2,
