import selectionSort from "../../code/sort/selectionSort";

test("selectionSort", () => {
  expect(selectionSort([3, 2, 1])).toEqual([1, 2, 3]);
});
