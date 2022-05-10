import selectionSort from './selectionSort';
import quickSort from './quickSort';
import mergeSort from './mergeSort';

const algorithms = {
  bubbleSort,
  insertionSort,
  selectionSort,
  quickSort,
  mergeSort,
};

const getResult = async (algorithmName, array) => {
  const algorithm = algorithms[algorithmName];
  const start = Date.now();
  const result = await algorithm(array);
  const end = Date.now();
  const time = end - start;
  return {
    time,
    result,
  };
};

export default getResult;
