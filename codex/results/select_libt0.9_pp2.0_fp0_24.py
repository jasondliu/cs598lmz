import selector from '../../selector';

export default (state) => {

    const getMyForm = (formId) => {
        const formPosition = state.myForms.myFormIds.indexOf(formId);
        if (formPosition === -1) {
            return null;
        }
        return state.myForms.myForms[state.myForms.myFormIds[formPosition]];
    };

    return {
        ...state,
        getMyForm,
        isFetchingMyForms: (state.myForms || {}).fetchingForms,
        ...selector(state)
    };
};
