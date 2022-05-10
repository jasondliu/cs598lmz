import select from '../select'

describe('select', () => {
  test('can call', () => {
    const result = select('#app')
    expect(result).toBeDefined()
  })

  test('can query with scoped query', () => {
    const result = select(':scope > div', document.getElementById('app'))
    expect(result.length).toBe(1)
  })
})
