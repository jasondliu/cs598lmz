import select from 'select-dom'

export default function () {
  const container = select('.file-navigation')
  const sidebar = document.querySelector('.repository-content .repository-sidebar')
  const sidebarHeight = sidebar.clientHeight
  let containerTop = container.offsetTop
  containerTop -= sidebarHeight - container.clientHeight
  const top = containerTop - window.pageYOffset
  if (top < 0) {
    const newTop = window.pageYOffset + top
    window.scrollTo(0, newTop)
  }
}
