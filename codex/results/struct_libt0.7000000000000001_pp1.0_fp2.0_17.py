import _struct from './struct'

const withInfo = story => {
  return <div style={{ margin: '1rem' }}>{story()}</div>
}

const fieldOptions = [
  {
    label: 'Name',
    value: 'name'
  },
  {
    label: 'E-Mail',
    value: 'email'
  },
  {
    label: 'Phone',
    value: 'phone'
  }
]

const keyOptions = [
  {
    label: 'Business Key 1',
    value: 'businessKey1'
  },
  {
    label: 'Business Key 2',
    value: 'businessKey2'
  }
]

const stories = storiesOf('Struct', module)
  .addDecorator(withKnobs)
  .addDecorator(withInfo)

stories.add('Basic', () => {
  const value = {
    name: 'Willy Wonka',
    email: 'willy@example.com',
    phone: '123456',
    businessKey1:
