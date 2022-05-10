import selection.Selection;

public class SelectionSort implements Sort {

	private Selection selectionService;

	public SelectionSort(Selection selectionService) {

		this.selectionService = selectionService;
	}

	@Override
	public void sort(int[] array) {

		int length = array.length;

		int minIndex;
		for (int i = 0; i < length; i++) {
			minIndex = selectionService.findMinIndex(array, i, length);
			if (i != minIndex) {
				swap(array, i, minIndex);
			}
		}

	}

	private void swap(int[] array, int minIndex, int i) {
		int temp = array[i];
		array[i] = array[minIndex];
		array[minIndex] = temp;
	}

}
