import selection from './selection';

export default function select(type, state) {
    if (selection.type === type) {
        return;
    }

    selection.type = type;

    // When changing selection type, make sure to rerender canvas,
    // as a different selection type may be rendered differently
    render(state);
}
