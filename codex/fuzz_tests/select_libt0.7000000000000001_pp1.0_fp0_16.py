import selectionSetToArray from "../selectionSetToArray";

export default function parseSelectionSet(selectionSet) {
  const arrayOfSelection = selectionSetToArray(selectionSet);
  return arrayOfSelection.reduce(
    (acc, selection) =>
      selection.kind === "Field"
        ? {
            ...acc,
            data: {
              ...acc.data,
              [selection.name.value]: selection.selectionSet
                ? parseSelectionSet(selection.selectionSet)
                : true
            }
          }
        : acc,
    { data: {}, errors: [] }
  );
}
