import selector from './selector';

const mapStateToProps = (state) => {
    return {
        data: selector(state),
    };
};

const mapDispatchToProps = (dispatch) => {
    return {
        onSubmit: (data) => {
            dispatch(actionCreator.doAddOrUpdate(data));
        },
        onCancel: () => {
            dispatch(actionCreator.doCloseModal());
        },
    };
};

export default connect(mapStateToProps, mapDispatchToProps)(ModalForm);
