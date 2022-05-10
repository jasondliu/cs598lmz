import selection_sort.SelectionSort;

public class Test {

    public static void main(String[] args) {

        Test test = new Test();
        test.testBinarySearch();
        test.testLineSearch();
        test.testSelectionSearch();
    }

    public void testBinarySearch() {
        int[] arr = new int[]{1, 2, 3, 5, 8, 9, 11, 17, 25};
        System.out.println(arr.toString());
        int position1 = BinarySearch.search(arr, 9);
        System.out.println("position of 9 is: " + position1);
        System.out.println();

        int[] arr2 = new int[]{1, 2, 3, 4, 5, 8, 9, 11, 13, 17, 22, 24, 26, 29};
        System.out.println(arr2.toString());
        int position2 = BinarySearch.search(arr2, 26);
        System.out.println("position of 26 is: " + position2);
        System.out.println();
    }

    public
