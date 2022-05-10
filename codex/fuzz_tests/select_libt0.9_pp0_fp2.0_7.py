import select from 'select'

import Field from './Field'
import FieldGroup from './FieldGroup'
import { primaryColor } from './palette'

export class SelectField extends Field {
  static propTypes = {
    value: PropTypes.string,
    onChange: PropTypes.func,
    onBlur: PropTypes.func,
    onFocus: PropTypes.func,
    options: PropTypes.array,
    multiple: PropTypes.bool,
  };
  static defaultProps = {
    autoComplete: 'off',
    autoCorrect: 'off',
    autoCapitalize: 'off',
    spellCheck: 'off',
    role: 'select',
  };
  blur() {
    const { DOMNode } = this.refs
    DOMNode.blur()
  }
  focus() {
    const { DOMNode } = this.refs
    DOMNode.focus()
  }
  render() {
    const {
      placeholder,
      value,
      onChange,
      onBlur,
      onFocus,
      height,
