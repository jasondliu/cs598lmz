import selector from './selector'

import {
  mapDispatchToProps,
  mapStateToProps
} from './connect'

import Style from './Style'

class Component extends React.PureComponent {
  render () {
    const {
      store,
      styles,
    } = this.props
    const {
      session,
    } = store
    return (
      <div
        className={classNames.container}
        style={styles.container}
      >
        <div
          className={classNames.content}
          style={styles.content}
        >
          <div
            className={classNames.title}
            style={styles.title}
          >
            {session.title}
          </div>
          <div
            className={classNames.summary}
            style={styles.summary}
          >
            {session.summary}
          </div>
        </div>
      </div>
    )
  }

  componentDidMount () {
    const {
      store,
      actions,
    }
