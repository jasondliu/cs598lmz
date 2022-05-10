import _struct from '../_/struct'

export default _struct({
  id: string,
  title: string,
  description: string,
  createdAt: number,
  updatedAt: number,
  assignees: [string],
}, { assignees: [] })
