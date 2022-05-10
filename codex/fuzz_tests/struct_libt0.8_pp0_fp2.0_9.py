import _struct from './_struct';

export default _struct({
  displayName: _struct.string(),
  id: _struct.string(),
  imageUrl: _struct.string(),
  type: _struct.literal('server'),
  serverId: _struct.optional(_struct.string()),
}, 'TeamMember');
