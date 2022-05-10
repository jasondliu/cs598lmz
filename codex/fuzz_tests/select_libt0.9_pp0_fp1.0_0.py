import selectionsort from '../../lib/sorts/selectionsort';

describe('selectionsort', function() {
  describe('sort', function() {
    it('sorts an empty array', function() {
      assert.deepEqual(selectionsort.sort([]), []);
    });

    it('sorts a single-element array', function() {
      assert.deepEqual(selectionsort.sort([5]), [5]);
    });

    it('sorts a longer array', function() {
      assert.deepEqual(selectionsort.sort([6, 5, 1, 2, 9]), [1, 2, 5, 6, 9]);
    });

    it('sorts an array with duplicate elements', function() {
      assert.deepEqual(selectionsort.sort([6, 9, 6, 5]), [5, 6, 6, 9]);
    });

    it('sorts a reverse-sorted array', function() {
      assert.deepEqual(selectionsort.sort([9, 8, 7, 6, 5]), [5, 6, 7, 8,
