import selectByVisibleText from '../scripts/selectByVisibleText';

describe('selectByVisibleText', () => {
  it('should select the element with the visible text', async () => {
    const page = getQueryFn(createStaticPage());
    const query = mapResults(
      page,
      selectByVisibleText('Option 2'),
      elements => elements[1].value
    );

    const results = await query('select');

    expect(results).toEqual(['2']);
  });

  it('should select all elements with the visible text', async () => {
    const page = getQueryFn(createStaticPage());
    const query = mapResults(
      page,
      selectByVisibleText('Option'),
      elements => elements[1].value
    );

    const results = await query('select');

    expect(results).toEqual(['1', '2', '3']);
  });
});
