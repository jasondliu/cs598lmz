import selectForUpdate from '../helpers/selectForUpdate';

const cursor = {
  async update(
    {
      _id,
      ...update
    },
    { collection, context },
  ) {
    const {
      afterUpdate,
      auth,
      beforeUpdate,
      collectionHooks,
      db,
      hooks,
      typeName,
    } = context;

    const result = await collectionHooks.wrapMutateCall(
      async () => {
        const hookResult = await beforeUpdate(update, {
          document: {
            _id,
          },
          collection,
          context,
          typeName,
        });

        const hasMutated = await updateDocument({
          db,
          collection,
          hookResult,
          _id,
          update,
          context,
          auth,
        });

        if (!hasMutated) return {};

        const { transformedDoc, transformedUpdate } = hookResult;
        const doc = transformedDoc
          || (await selectForUpdate(
            { db, collection, selector: { _id } },
