import selectorFactory from '../selectors'

describe('jobDetail selector', () => {
  describe('all', () => {
    const selector = selectorFactory('jobDetail', 'all')
    it('returns the state', () => {
      expect(selector({ jobDetail: { all: 'foo' } })).toBe('foo')
    })
  })

  describe('byId', () => {
    const selector = selectorFactory('jobDetail', 'byId')
    it('returns the state', () => {
      expect(selector({ jobDetail: { byId: 'bar' } })).toBe('bar')
    })
  })
})
