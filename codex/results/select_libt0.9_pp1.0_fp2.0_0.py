import select from 'select'
import Emitter from 'emitter'
import reduce from 'reduce-component'
import css from 'css'

/**
 * Export `List`
 */

export default class List extends Component {

  /**
   * Initialize
   */

  constructor(data = []) {
    super()
    this.on('mount', () => {
      this.data = this.refs.data.value
    })

    this.on('update', () => {
      this.data = this.refs.data.value
    })

    this.refs.data.value = data
  }

  /**
   * Add
   */

  add(content) {
    this.data.push(content)
    this.update()
  }

  /**
   * Remove
   */

  remove(index) {
    this.data.splice(index, 1)
    this.update()
  }

  /**
   * Select
   */

  select(index) {
    el = this.refs[`list-${index}`]
