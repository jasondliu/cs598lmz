import selectedFilters from '../filtersSelector';

describe('Filters Selector', () => {
    it ('should return all filters', () => {
        const filter = 'something';
        const mockState = {
            filters: {
                text: filter,
                sortBy: 'amount',
                startDate: undefined,
                endDate: undefined
            }
        };

        const result = selectedFilters(mockState);
        expect(result).toEqual(mockState.filters);
    });
});
