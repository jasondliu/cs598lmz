import selectionSort from '../selectionSort/index';
import quickSort from '../quickSort/index';
import mergeSort from '../mergeSort/index';

export function getSortNumber(sortName) {
  const sortMap = {
    RUN: runSort,
    BUBBLE: bubbleSort,
    INSERT: insertSort,
    SELECTION: selectionSort,
    QUICK: quickSort,
    MERGE: mergeSort,
  };
  return sortMap[sortName];
}
