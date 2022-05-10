import selectorFactory from './selectorFactory';

export default function(mapStateToProps) {
  const selector = selectorFactory(mapStateToProps);
  return (state, props) => selector(state, props);
}
