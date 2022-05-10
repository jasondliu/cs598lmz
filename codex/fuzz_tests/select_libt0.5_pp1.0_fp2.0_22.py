import selector from './selector';
import { getId, arrayify } from '@scipe/jsonld';
import { getObjectId } from '../utils/schema-utils';

export default function createId(
  action,
  { now, store, prevAction, skipPayloadValidation } = {}
) {
  if (!action['@id']) {
    const objectId = getObjectId(action);
    if (objectId) {
      const object = store.getState().getIn(['graph', objectId]);
      if (object) {
        const actionType = arrayify(object.action)
          .filter(a => getId(a) === getId(action))
          .map(a => a['@type'])
          .filter(Boolean)[0];

        if (actionType) {
          const createId = selector(objectId, actionType, {
            store,
            now,
            prevAction,
            skipPayloadValidation
          });
          if (createId) {
            return createId;
          }
        }
      }

