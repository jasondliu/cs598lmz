import selectedSearchStore from './stores'
import { makeComponent } from '../../core/component'
import { getSearchId } from '../../core/utils'

/**
 * Component with the search store as props
 * @param {Function} mapState - Function to map the state of the store to the props
 */
export default function withSearchStore(mapState) {
  return function(Component) {
    return makeComponent(Component, selectedSearchStore, mapState)
  }
}

/**
 * Injects the search store into the props of a component
 * @param {Function} mapState - Function to map the state of the store to the props
 */
export function injectSearchStore(...mapStateArgs) {
  return function(WrappedComponent) {
    const Component = withSearchStore(...mapStateArgs)(WrappedComponent)

    function Wrapper(props) {
      const { widgetId, contextId } = props
      const searchId = getSearchId(contextId, widgetId)

      return <Component selectedSearchId={searchId} {...props} />
    }

    Wrapper
