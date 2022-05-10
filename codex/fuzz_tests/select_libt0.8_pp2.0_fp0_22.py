import selectTagsByType from './selectTagsByType'

export default (
  state,
  {
    theme: {
      breakpoints: { down },
      mediaQueries
    }
  } = {}
) => {
  const breakpoints = selectBreakpoints(state)
  const text = selectText(state)
  const { tags } = selectData(state)

  return [
    ...(selectTagsByType('article', tags) || []).map(
      ({ id, slug, title, image, categories }) => {
        const isSmall = breakpoints.some(({ path }) => down(path))
        const paddingTop = isSmall ? '56.25%' : '50%'

        return {
          component: 'article',
          id,
          key: id,
          paddingTop,
          to: slug,
          children: [
            {
              component: 'Picture',
              key: image,
              image,
              width: '100%',
              height: '100%'
            },
            {
              component: 'Section',
              key: 'section
