import selectionSort from "./selectionSort";
import { SortedArray } from "./SortedArray";
import { render } from "@testing-library/react";

main();

function testSort(testNumbers: number[], sortedNumbers: number[], sortedArray: SortedArray) {
  sort(testNumbers, sortedArray, (a, b) => a - b);
  expect(testNumbers).toEqual(sortedNumbers);
  expect(sortedArray.isSorted(sortedNumbers.length, (a, b) => a - b)).toBe(true);
}

function main() {
  let randomNumbers: number[] = [];
  let sortedNumbers: number[] = [];
  let sortedArray: SortedArray | null = null;
  describe("random numbers", function () {
    beforeEach(() => {
      randomNumbers = [];
      sortedNumbers = [];
      const n = 50;
      for (let i = 0; i < n; ++i) {
        const num = Math.floor(Math.random() * 100);
        sortedNumbers.push(num);
       
