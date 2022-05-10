import selection from '../selection'
import { matches, getOffset } from '../dom'
import { sandbox, innerHTML } from '../test-helpers'

const content = '<div id="sandbox">test</div>'

beforeEach(() => {
  sandbox.innerHTML = content
})

test('sets destination range and scrolls to it', async () => {
  const div = sandbox.querySelector('div')
  const el = document.createElement('span')
  const from = {
    container: div,
    offset: 0,
  }
  const to = {
    container: el,
    offset: 1,
  }

  document.body.appendChild(el)
  try {
    sandbox.scrollTop = 100
    sandbox.scrollLeft = 100

    // Mock scrollTo behavior
    global.scrollTo = jest.fn()

    selection.set({ from, to })

    // Make sure to use flush to ensure scrollTo is called
    await flush(true)

    expect(global.scrollTo).toHaveBeenCalledWith(0, 0)
